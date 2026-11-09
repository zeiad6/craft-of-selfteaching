"""Render high-definition 1080p MP4 explainer videos with polished UI/UX design.

Features:
  - Deep dark gradient canvas with ambient lighting & grid
  - macOS-style Code Editor / Terminal showcase with line numbers
  - Floating frosted-glass narration subtitle bar with soundwave icon
  - Dynamic scene progress indicators & neon bottom progress bar
  - Full RTL/LTR typography with arabic_reshaper & python-bidi
  - Lightning-fast H.264 rendering via imageio-ffmpeg & edge-tts
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
        try:
            return ImageFont.truetype(str(path), size)
        except Exception:
            pass
    return ImageFont.load_default()


def shape_text(text: str, is_arabic: bool) -> str:
    if not is_arabic:
        return text
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


def wrap_text(text: str, max_chars: int = 55) -> list[str]:
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


def create_gradient_background(width: int, height: int) -> Image.Image:
    """Create a vertical gradient background with subtle ambient glows."""
    base = Image.new("RGB", (width, height), (10, 14, 23))
    draw = ImageDraw.Draw(base)

    # Vertical gradient stripes
    for y in range(0, height, 4):
        ratio = y / height
        r = int(10 + (22 - 10) * ratio)
        g = int(14 + (24 - 14) * ratio)
        b = int(23 + (45 - 23) * ratio)
        draw.rectangle([(0, y), (width, y + 4)], fill=(r, g, b))

    # Subtle grid lines
    grid_color = (255, 255, 255, 10)
    for x in range(0, width, 120):
        draw.line([(x, 0), (x, height)], fill=(20, 28, 45), width=1)
    for y in range(0, height, 90):
        draw.line([(0, y), (width, y)], fill=(20, 28, 45), width=1)

    return base


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
    img = create_gradient_background(width, height)
    draw = ImageDraw.Draw(img)

    # 1. Top Navigation Bar (Header)
    # Python 3.12 badge (Left)
    draw.rounded_rectangle([(70, 38), (250, 84)], radius=14, fill=(15, 23, 42), outline=(56, 189, 248), width=1)
    draw.ellipse([(88, 55), (100, 67)], fill=(56, 189, 248))
    badge_font = get_font("segoeui.ttf", 20)
    draw.text((112, 48), "Python 3.12+", fill=(226, 232, 240), font=badge_font)

    # Series Brand Title (Center)
    brand = "فن التعلّم الذاتي  •  The Craft of Self-Teaching"
    brand_font = get_font("segoeui.ttf", 22)
    draw.text((280, 50), shape_text(brand, is_ar), fill=(148, 163, 184), font=brand_font)

    # Scene Tracker Pill (Right)
    draw.rounded_rectangle([(1550, 38), (1850, 84)], radius=14, fill=(15, 23, 42), outline=(129, 140, 248), width=1)
    # Mini tracker dots: e.g. [● ● ○ ○]
    dots = " ".join("●" if i <= scene_idx else "○" for i in range(1, total_scenes + 1))
    tracker_label = f"{dots}  ({scene_idx}/{total_scenes})"
    tracker_font = get_font("segoeui.ttf", 19)
    draw.text((1575, 49), tracker_label, fill=(199, 210, 254), font=tracker_font)

    # 2. Main Chapter Title Header
    ch_font = get_font("segoeui.ttf", 44)
    draw.text((70, 102), shape_text(chapter_title, is_ar), fill=(255, 255, 255), font=ch_font)

    # Glowing subtle divider
    draw.line([(70, 168), (1850, 168)], fill=(30, 41, 59), width=2)
    draw.line([(70, 168), (350, 168)], fill=(56, 189, 248), width=2)

    # 3. Center Showcase Card (macOS Window Style)
    card_x1, card_y1, card_x2, card_y2 = 70, 195, 1850, 775
    # Outer card border with glow
    draw.rounded_rectangle([(card_x1, card_y1), (card_x2, card_y2)], radius=20, fill=(15, 23, 42), outline=(51, 65, 85), width=2)

    # Window Header Bar
    tab_height = 56
    draw.rounded_rectangle([(card_x1, card_y1), (card_x2, card_y1 + tab_height)], radius=20, fill=(24, 33, 54))
    draw.rectangle([(card_x1, card_y1 + 30), (card_x2, card_y1 + tab_height)], fill=(24, 33, 54))
    draw.line([(card_x1, card_y1 + tab_height), (card_x2, card_y1 + tab_height)], fill=(51, 65, 85), width=1)

    # Window Action Dots (🔴 🟡 🟢)
    dot_y = card_y1 + 22
    draw.ellipse([(95, dot_y), (111, dot_y + 16)], fill=(239, 68, 68))
    draw.ellipse([(121, dot_y), (137, dot_y + 16)], fill=(245, 158, 11))
    draw.ellipse([(147, dot_y), (163, dot_y + 16)], fill=(16, 185, 129))

    # Editor Tab Pill
    draw.rounded_rectangle([(195, card_y1 + 10), (450, card_y1 + tab_height - 6)], radius=10, fill=(15, 23, 42), outline=(56, 189, 248), width=1)
    tab_font = get_font("segoeui.ttf", 20)
    draw.text((215, card_y1 + 16), "⚡ main.py  •  Interactive Concept", fill=(147, 197, 253), font=tab_font)

    # Scene Title Badge inside Editor
    scene_badge = f"📌 {scene_title}"
    badge_font_scene = get_font("segoeui.ttf", 24)
    draw.text((1500, card_y1 + 14), shape_text(scene_badge, is_ar), fill=(251, 191, 36), font=badge_font_scene)

    # 4. Code & Visual Concept Content Pane
    # Left Gutter / Line Numbers Pane
    gutter_x = card_x1 + 65
    draw.line([(gutter_x, card_y1 + tab_height), (gutter_x, card_y2)], fill=(30, 41, 59), width=1)

    line_no_font = get_font("segoeui.ttf", 22)
    vis_font = get_font("segoeui.ttf", 34)
    vis_lines = wrap_text(visual_desc, max_chars=54 if not is_ar else 42)

    content_y = card_y1 + tab_height + 40
    for idx, line in enumerate(vis_lines[:7], 1):
        # Line number
        draw.text((card_x1 + 22, content_y + 5), f"{idx:02d}", fill=(71, 85, 105), font=line_no_font)

        # Content text (with RTL handling)
        shaped_line = shape_text(line, is_ar)
        # Give keyword/syntax glow to text
        draw.text((gutter_x + 35, content_y), shaped_line, fill=(241, 245, 249), font=vis_font)
        content_y += 62

    # 5. Floating Subtitle Pill at Bottom
    sub_x1, sub_y1, sub_x2, sub_y2 = 70, 810, 1850, 1030
    draw.rounded_rectangle([(sub_x1, sub_y1), (sub_x2, sub_y2)], radius=22, fill=(15, 23, 42), outline=(56, 189, 248), width=2)

    # Narration Header & Audio Waveform graphic
    aud_label = "🎙️ التعليق الصوتي المباشر (Narration):" if is_ar else "🎙️ Real-time Narration:"
    aud_hdr_font = get_font("segoeui.ttf", 22)
    draw.text((sub_x1 + 35, sub_y1 + 18), shape_text(aud_label, is_ar), fill=(251, 191, 36), font=aud_hdr_font)

    # Stylized Audio Waves (Right side of narration header)
    wave_x = sub_x2 - 160
    wave_bars = [12, 22, 34, 18, 28, 14, 26, 10, 20]
    for w_idx, b_height in enumerate(wave_bars):
        bx = wave_x + (w_idx * 12)
        by1 = sub_y1 + 32 - (b_height // 2)
        by2 = sub_y1 + 32 + (b_height // 2)
        draw.rounded_rectangle([(bx, by1), (bx + 5, by2)], radius=2, fill=(56, 189, 248))

    # Narration Subtitle Text (Crisp & Readable)
    aud_font = get_font("segoeui.ttf", 32)
    aud_lines = wrap_text(audio_text, max_chars=72 if not is_ar else 58)
    aud_y = sub_y1 + 65
    for line in aud_lines[:3]:
        shaped_line = shape_text(line, is_ar)
        draw.text((sub_x1 + 35, aud_y), shaped_line, fill=(248, 250, 252), font=aud_font)
        aud_y += 46

    # 6. Bottom Neon Progress Bar
    progress_ratio = scene_idx / total_scenes
    draw.rectangle([(0, height - 8), (width, height)], fill=(15, 23, 42))
    draw.rectangle([(0, height - 8), (int(width * progress_ratio), height)], fill=(56, 189, 248))

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

        # 1. Synthesize Audio via Edge-TTS
        await generate_audio(scene["audio"], voice, audio_path)

        # 2. Render High-Definition Slide Frame
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

    # 4. Concatenate into Final Master Video
    final_video_path = OUTPUT_DIR / f"{lang}_{chapter_slug}.mp4"
    concatenate_scenes(scene_mp4s, final_video_path)
    file_size_mb = final_video_path.stat().st_size / (1024 * 1024)
    print(f"✅ Generated master video: {final_video_path.name} ({file_size_mb:.2f} MB)")
    return final_video_path


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", choices=["ar", "en", "both"], default="both")
    parser.add_argument("--chapter", default=None, help="e.g. 00-preface or 01-getting-started")
    parser.add_argument("--all", action="store_true", help="Render all chapters")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    langs = ["ar", "en"] if args.lang == "both" else [args.lang]

    for l in langs:
        if args.chapter:
            await render_chapter(l, args.chapter)
        else:
            scripts = sorted((VIDEOS_DIR / l).glob("*.md"))
            for s in scripts:
                await render_chapter(l, s.stem)


if __name__ == "__main__":
    asyncio.run(main())
