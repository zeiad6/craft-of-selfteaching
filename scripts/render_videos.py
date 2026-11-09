"""Render full 1080p MP4 explainer videos from chapter video scripts.

Uses:
  - edge-tts (neural voiceover: ar-SA-HamedNeural / en-US-AriaNeural)
  - Pillow + arabic_reshaper + python-bidi (1080p slide generation)
  - imageio-ffmpeg (fast H.264 video assembly and concatenation)

Usage:
  python scripts/render_videos.py --lang ar --chapter 00-preface
  python scripts/render_videos.py --lang en --chapter 01-getting-started
  python scripts/render_videos.py --lang ar --all
"""
import argparse
import asyncio
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import arabic_reshaper
from bidi.algorithm import get_display
import edge_tts
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
VIDEOS_DIR = ROOT / "videos"
OUTPUT_DIR = VIDEOS_DIR / "rendered"
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

VOICES = {
    "ar": "ar-SA-HamedNeural",
    "en": "en-US-AriaNeural"
}

FONT_DIR = Path(os.environ.get("WINDIR", "C:\\Windows")) / "Fonts"


def get_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    path = FONT_DIR / name
    if path.exists():
        return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def shape_text(text: str, is_arabic: bool) -> str:
    if not is_arabic:
        return text
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


def wrap_text(text: str, max_chars: int = 60) -> list[str]:
    words = text.split()
    lines = []
    curr = []
    curr_len = 0
    for w in words:
        if curr_len + len(w) + 1 <= max_chars:
            curr.append(w)
            curr_len += len(w) + 1
        else:
            if curr:
                lines.append(" ".join(curr))
            curr = [w]
            curr_len = len(w)
    if curr:
        lines.append(" ".join(curr))
    return lines


def parse_script(md_path: Path) -> dict:
    content = md_path.read_text(encoding="utf-8")
    title_match = re.search(r"^# 🎬 [^:]+:\s*(.+)$", content, re.M)
    title = title_match.group(1).strip() if title_match else md_path.stem

    scenes = []
    scene_blocks = re.split(r"^## (?:Scene|المشهد)\s+\d+:\s*", content, flags=re.M)[1:]
    for block in scene_blocks:
        lines = block.strip().splitlines()
        scene_title = lines[0].strip() if lines else "Scene"
        vis_match = re.search(r"\*\*(?:Visual|ما يظهر على الشاشة[^:]*):\*\*\s*(.+)$", block, re.M)
        aud_match = re.search(r"\*\*(?:Audio|الكلام[^:]*):\*\*\s*(.+)$", block, re.M)
        scenes.append({
            "title": scene_title,
            "visual": vis_match.group(1).strip() if vis_match else "",
            "audio": aud_match.group(1).strip() if aud_match else ""
        })
    return {"title": title, "scenes": scenes}


async def generate_audio(text: str, voice: str, out_path: Path):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(out_path))


def create_scene_frame(
    lang: str,
    chapter_title: str,
    scene_idx: int,
    total_scenes: int,
    scene_title: str,
    visual_desc: str,
    audio_text: str,
    out_img_path: Path
):
    is_ar = (lang == "ar")
    width, height = 1920, 1080
    img = Image.new("RGB", (width, height), (10, 14, 23))
    draw = ImageDraw.Draw(img)

    # Decorative header bar
    draw.rectangle([(0, 0), (width, 10)], fill=(56, 189, 248))

    # Top brand / chapter tag
    brand = "فن التعلّم الذاتي | The Craft of Self-Teaching"
    tag_font = get_font("segoeui.ttf", 26)
    draw.text((80, 50), shape_text(brand, is_ar), fill=(148, 163, 184), font=tag_font)

    # Scene counter pill
    counter_text = f"Scene {scene_idx}/{total_scenes}" if not is_ar else f"المشهد {scene_idx} من {total_scenes}"
    draw.rounded_rectangle([(1600, 42), (1840, 90)], radius=12, fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    cnt_font = get_font("segoeui.ttf", 22)
    draw.text((1630, 52), shape_text(counter_text, is_ar), fill=(226, 232, 240), font=cnt_font)

    # Main Chapter Header
    ch_font = get_font("segoeui.ttf", 46)
    draw.text((80, 105), shape_text(chapter_title, is_ar), fill=(255, 255, 255), font=ch_font)
    draw.line([(80, 175), (1840, 175)], fill=(30, 41, 59), width=2)

    # Center Hero Card (The Visual Concept)
    draw.rounded_rectangle([(80, 210), (1840, 780)], radius=24, fill=(17, 24, 39), outline=(51, 65, 85), width=2)

    # Card Title Badge
    draw.rounded_rectangle([(120, 240), (450, 290)], radius=10, fill=(30, 41, 59))
    scene_tag_font = get_font("segoeui.ttf", 24)
    draw.text((140, 250), shape_text(f"📌 {scene_title}", is_ar), fill=(56, 189, 248), font=scene_tag_font)

    # Visual Concept Box
    draw.rounded_rectangle([(120, 315), (1800, 740)], radius=16, fill=(10, 14, 23), outline=(30, 41, 59), width=1)

    # Mac-style terminal dots
    draw.ellipse([(145, 335), (161, 351)], fill=(239, 68, 68))
    draw.ellipse([(171, 335), (187, 351)], fill=(245, 158, 11))
    draw.ellipse([(197, 335), (213, 351)], fill=(16, 185, 129))

    # Visual Description Content
    vis_font = get_font("segoeui.ttf", 36)
    vis_lines = wrap_text(visual_desc, max_chars=55 if not is_ar else 45)
    y_offset = 400
    for line in vis_lines:
        shaped_line = shape_text(line, is_ar)
        draw.text((160, y_offset), shaped_line, fill=(226, 232, 240), font=vis_font)
        y_offset += 60

    # Modern Subtitle / Audio Box at the Bottom
    draw.rounded_rectangle([(80, 815), (1840, 1025)], radius=20, fill=(15, 23, 42), outline=(56, 189, 248), width=2)
    aud_badge_font = get_font("segoeui.ttf", 20)
    draw.text((120, 835), shape_text("🎙️ التعليق الصوتي (Narration):" if is_ar else "🎙️ Narration:", is_ar), fill=(251, 191, 36), font=aud_badge_font)

    aud_font = get_font("segoeui.ttf", 30)
    aud_lines = wrap_text(audio_text, max_chars=75 if not is_ar else 60)
    aud_y = 880
    for line in aud_lines[:3]:
        shaped_line = shape_text(line, is_ar)
        draw.text((120, aud_y), shaped_line, fill=(241, 245, 249), font=aud_font)
        aud_y += 42

    img.save(str(out_img_path), format="PNG")


def render_scene_video(img_path: Path, audio_path: Path, out_mp4_path: Path):
    cmd = [
        FFMPEG,
        "-y",
        "-loop", "1",
        "-i", str(img_path),
        "-i", str(audio_path),
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        str(out_mp4_path)
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def concatenate_scenes(scene_mp4s: list[Path], final_mp4: Path):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        for p in scene_mp4s:
            # Escape path for ffmpeg concat demuxer
            safe_path = str(p.resolve()).replace("\\", "/")
            f.write(f"file '{safe_path}'\n")
        concat_txt = Path(f.name)

    try:
        cmd = [
            FFMPEG,
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_txt),
            "-c", "copy",
            str(final_mp4)
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        if concat_txt.exists():
            concat_txt.unlink()


async def render_chapter(lang: str, chapter_slug: str):
    script_file = VIDEOS_DIR / lang / f"{chapter_slug}.md"
    if not script_file.exists():
        print(f"Error: {script_file} not found!")
        return None

    data = parse_script(script_file)
    chapter_title = data["title"]
    scenes = data["scenes"]
    print(f"\n🎬 Rendering [{lang.upper()}] {chapter_title} ({len(scenes)} scenes)...")

    work_dir = OUTPUT_DIR / lang / chapter_slug
    work_dir.mkdir(parents=True, exist_ok=True)
    voice = VOICES[lang]

    scene_mp4s = []
    for idx, scene in enumerate(scenes, 1):
        print(f"  → Scene {idx}/{len(scenes)}: {scene['title']}")
        audio_path = work_dir / f"scene_{idx:02d}.mp3"
        img_path = work_dir / f"scene_{idx:02d}.png"
        mp4_path = work_dir / f"scene_{idx:02d}.mp4"

        # 1. Synthesize Audio
        await generate_audio(scene["audio"], voice, audio_path)

        # 2. Render Slide Image
        create_scene_frame(
            lang=lang,
            chapter_title=chapter_title,
            scene_idx=idx,
            total_scenes=len(scenes),
            scene_title=scene["title"],
            visual_desc=scene["visual"],
            audio_text=scene["audio"],
            out_img_path=img_path
        )

        # 3. Render Scene Video
        render_scene_video(img_path, audio_path, mp4_path)
        scene_mp4s.append(mp4_path)

    # 4. Concatenate into Final Chapter Video
    final_video_path = OUTPUT_DIR / f"{lang}_{chapter_slug}.mp4"
    concatenate_scenes(scene_mp4s, final_video_path)
    file_size_mb = final_video_path.stat().st_size / (1024 * 1024)
    print(f"✅ Generated final chapter video: {final_video_path.name} ({file_size_mb:.2f} MB)")
    return final_video_path


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", choices=["ar", "en"], default="ar")
    parser.add_argument("--chapter", default="00-preface", help="e.g. 00-preface or 01-getting-started")
    parser.add_argument("--all", action="store_true", help="Render all chapters")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        scripts = sorted((VIDEOS_DIR / args.lang).glob("*.md"))
        for s in scripts:
            await render_chapter(args.lang, s.stem)
    else:
        await render_chapter(args.lang, args.chapter)


if __name__ == "__main__":
    asyncio.run(main())
