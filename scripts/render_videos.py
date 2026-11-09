"""Render high-definition 1080p MP4 explainer videos with polished UI/UX design.

Features:
  - Deep dark gradient canvas with ambient lighting & tech grid
  - macOS-style Code Editor / Terminal showcase with authentic, non-translated Python code
  - Syntax highlighting: keywords, strings, comments, builtins, and decorators
  - Floating frosted-glass narration subtitle bar with soundwave visualizer
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

ROOT = Path(__file__).resolve().parent.parent
VIDEOS_DIR = ROOT / "videos"
OUTPUT_DIR = VIDEOS_DIR / "rendered"
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

sys.path.insert(0, str(ROOT / "scripts"))
from code_snippets import CHAPTER_SNIPPETS

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

VOICES = {
    "ar": "ar-SA-HamedNeural",
    "en": "en-US-AriaNeural"
}

FONT_DIR = Path(os.environ.get("WINDIR", "C:\\Windows")) / "Fonts"

KEYWORDS = {
    "def", "return", "class", "import", "from", "if", "elif", "else",
    "match", "case", "for", "in", "while", "break", "continue", "try",
    "except", "finally", "assert", "yield", "raise", "async", "await",
    "with", "as", "pass", "not", "and", "or", "is"
}

BUILTINS = {
    "print", "len", "range", "type", "int", "float", "str", "bool",
    "list", "dict", "set", "tuple", "enumerate", "zip", "sum", "min",
    "max", "Path", "dataclass", "open", "super", "round", "abs"
}

SYNTAX_COLORS = {
    "comment": (52, 211, 153),    # Emerald green
    "string": (251, 191, 36),     # Warm gold
    "keyword": (56, 189, 248),    # Vibrant cyan
    "builtin": (129, 140, 248),   # Indigo
    "decorator": (192, 132, 252), # Purple
    "number": (244, 114, 182),    # Pink
    "identifier": (248, 250, 252),# White
    "punct": (148, 163, 184)      # Slate
}


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
        if len(lines) >= 3:
            break
    if curr and len(lines) < 3:
        lines.append(" ".join(curr))
    return lines


def tokenize_code_line(line: str) -> list[tuple[str, str]]:
    """Tokenize a Python code line for syntax highlighting."""
    tokens = []
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if ch == "#":
            tokens.append((line[i:], "comment"))
            break
        elif ch in ('"', "'"):
            q = ch
            if line[i:i+3] == q * 3:
                end = line.find(q * 3, i + 3)
                if end == -1:
                    end = n - 3
                tokens.append((line[i:end+3], "string"))
                i = end + 3
            else:
                end = i + 1
                while end < n:
                    if line[end] == "\\":
                        end += 2
                    elif line[end] == q:
                        end += 1
                        break
                    else:
                        end += 1
                tokens.append((line[i:end], "string"))
                i = end
        elif ch.isalpha() or ch == "_":
            start = i
            while i < n and (line[i].isalnum() or line[i] == "_"):
                i += 1
            word = line[start:i]
            if word in KEYWORDS:
                tokens.append((word, "keyword"))
            elif word in BUILTINS:
                tokens.append((word, "builtin"))
            else:
                tokens.append((word, "identifier"))
        elif ch == "@":
            start = i
            i += 1
            while i < n and (line[i].isalnum() or line[i] == "_"):
                i += 1
            tokens.append((line[start:i], "decorator"))
        elif ch.isdigit():
            start = i
            while i < n and (line[i].isdigit() or line[i] == "."):
                i += 1
            tokens.append((line[start:i], "number"))
        else:
            tokens.append((ch, "punct"))
            i += 1
    return tokens


def draw_syntax_code_line(draw: ImageDraw.ImageDraw, x: int, y: int, line: str, font: ImageFont.FreeTypeFont):
    """Draw a syntax-highlighted line of code strictly LTR."""
    tokens = tokenize_code_line(line)
    curr_x = x
    for text_token, token_kind in tokens:
        color = SYNTAX_COLORS.get(token_kind, (248, 250, 252))
        draw.text((curr_x, y), text_token, fill=color, font=font)
        curr_x += int(font.getlength(text_token))


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
    base = Image.new("RGB", (width, height), (10, 14, 23))
    draw = ImageDraw.Draw(base)

    for y in range(0, height, 4):
        ratio = y / height
        r = int(10 + (22 - 10) * ratio)
        g = int(14 + (24 - 14) * ratio)
        b = int(23 + (45 - 23) * ratio)
        draw.rectangle([(0, y), (width, y + 4)], fill=(r, g, b))

    # Grid
    for x in range(0, width, 120):
        draw.line([(x, 0), (x, height)], fill=(20, 28, 45), width=1)
    for y in range(0, height, 90):
        draw.line([(0, y), (width, y)], fill=(20, 28, 45), width=1)

    return base


def create_scene_frame(
    lang: str,
    chapter_slug: str,
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
    draw.rounded_rectangle([(70, 36), (250, 82)], radius=14, fill=(15, 23, 42), outline=(56, 189, 248), width=1)
    draw.ellipse([(88, 53), (100, 65)], fill=(56, 189, 248))
    badge_font = get_font("segoeui.ttf", 20)
    draw.text((112, 46), "Python 3.12+", fill=(226, 232, 240), font=badge_font)

    # Series Brand Title (Center)
    brand = "فن التعلّم الذاتي  •  The Craft of Self-Teaching"
    brand_font = get_font("segoeui.ttf", 22)
    draw.text((280, 48), shape_text(brand, is_ar), fill=(148, 163, 184), font=brand_font)

    # Scene Tracker Pill (Right)
    draw.rounded_rectangle([(1550, 36), (1850, 82)], radius=14, fill=(15, 23, 42), outline=(129, 140, 248), width=1)
    dots = " ".join("●" if i <= scene_idx else "○" for i in range(1, total_scenes + 1))
    tracker_label = f"{dots}  ({scene_idx}/{total_scenes})"
    tracker_font = get_font("segoeui.ttf", 19)
    draw.text((1575, 47), tracker_label, fill=(199, 210, 254), font=tracker_font)

    # 2. Main Chapter Title Header
    ch_font = get_font("segoeuib.ttf", 40)
    draw.text((70, 98), shape_text(chapter_title, is_ar), fill=(255, 255, 255), font=ch_font)

    # Glowing subtle divider
    draw.line([(70, 158), (1850, 158)], fill=(30, 41, 59), width=2)
    draw.line([(70, 158), (350, 158)], fill=(56, 189, 248), width=2)

    # 3. Center Showcase Card (macOS Window Style)
    card_x1, card_y1, card_x2, card_y2 = 70, 178, 1850, 775
    draw.rounded_rectangle([(card_x1, card_y1), (card_x2, card_y2)], radius=18, fill=(15, 23, 42), outline=(51, 65, 85), width=2)

    # Window Header Bar
    tab_height = 52
    draw.rounded_rectangle([(card_x1, card_y1), (card_x2, card_y1 + tab_height)], radius=18, fill=(24, 33, 54))
    draw.rectangle([(card_x1, card_y1 + 25), (card_x2, card_y1 + tab_height)], fill=(24, 33, 54))
    draw.line([(card_x1, card_y1 + tab_height), (card_x2, card_y1 + tab_height)], fill=(51, 65, 85), width=1)

    # Window Action Dots (🔴 🟡 🟢)
    dot_y = card_y1 + 20
    draw.ellipse([(95, dot_y), (111, dot_y + 16)], fill=(239, 68, 68))
    draw.ellipse([(121, dot_y), (137, dot_y + 16)], fill=(245, 158, 11))
    draw.ellipse([(147, dot_y), (163, dot_y + 16)], fill=(16, 185, 129))

    # Editor Tab Pill
    draw.rounded_rectangle([(190, card_y1 + 8), (470, card_y1 + tab_height - 6)], radius=8, fill=(15, 23, 42), outline=(56, 189, 248), width=1)
    tab_font = get_font("segoeui.ttf", 19)
    draw.text((210, card_y1 + 14), "⚡ main.py  •  Python 3.12+", fill=(147, 197, 253), font=tab_font)

    # Scene Title Badge inside Editor Header
    badge_label = f"📌 المشهد {scene_idx}: {scene_title}" if is_ar else f"📌 Scene {scene_idx}: {scene_title}"
    badge_font_scene = get_font("segoeuib.ttf", 21)
    shaped_badge = shape_text(badge_label, is_ar)
    draw.text((1350, card_y1 + 14), shaped_badge, fill=(251, 191, 36), font=badge_font_scene)

    # 4. Code & Visual Concept Content Pane (Strictly Authentic Code, Never Translated)
    gutter_x = card_x1 + 65
    draw.line([(gutter_x, card_y1 + tab_height), (gutter_x, card_y2)], fill=(30, 41, 59), width=1)

    line_no_font = get_font("consola.ttf", 24)
    code_font = get_font("consola.ttf", 28)

    # Retrieve authentic code snippet for this chapter and scene
    snippets = CHAPTER_SNIPPETS.get(chapter_slug, [])
    if 0 <= scene_idx - 1 < len(snippets):
        raw_code = snippets[scene_idx - 1]
    else:
        raw_code = "# Python 3.12+\nprint('The Craft of Self-Teaching')\n"

    code_lines = raw_code.splitlines()

    content_y = card_y1 + tab_height + 30
    for idx, code_line in enumerate(code_lines[:9], 1):
        # Draw Line Number
        draw.text((card_x1 + 18, content_y + 2), f"{idx:02d}", fill=(71, 85, 105), font=line_no_font)

        # Draw Code strictly LTR (No Arabic translation or reshaping on code)
        draw_syntax_code_line(draw, gutter_x + 35, content_y, code_line, code_font)
        content_y += 54

    # 5. Floating Subtitle Pill at Bottom
    sub_x1, sub_y1, sub_x2, sub_y2 = 70, 795, 1850, 1025
    draw.rounded_rectangle([(sub_x1, sub_y1), (sub_x2, sub_y2)], radius=20, fill=(15, 23, 42), outline=(56, 189, 248), width=2)

    # Narration Header & Audio Waveform graphic
    aud_label = "🎙️ التعليق الصوتي المباشر (Narration):" if is_ar else "🎙️ Real-time Narration:"
    aud_hdr_font = get_font("segoeuib.ttf", 22)
    draw.text((sub_x1 + 35, sub_y1 + 16), shape_text(aud_label, is_ar), fill=(251, 191, 36), font=aud_hdr_font)

    # Stylized Audio Waves
    wave_x = sub_x2 - 160
    wave_bars = [12, 22, 34, 18, 28, 14, 26, 10, 20]
    for w_idx, b_height in enumerate(wave_bars):
        bx = wave_x + (w_idx * 12)
        by1 = sub_y1 + 30 - (b_height // 2)
        by2 = sub_y1 + 30 + (b_height // 2)
        draw.rounded_rectangle([(bx, by1), (bx + 5, by2)], radius=2, fill=(56, 189, 248))

    # Narration Subtitle Text (Crisp & Readable)
    aud_font = get_font("segoeui.ttf", 30)
    aud_lines = wrap_text(audio_text, max_chars=72 if not is_ar else 58)
    aud_y = sub_y1 + 60
    for line in aud_lines[:3]:
        shaped_line = shape_text(line, is_ar)
        draw.text((sub_x1 + 35, aud_y), shaped_line, fill=(248, 250, 252), font=aud_font)
        aud_y += 44

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

        # 2. Render High-Definition Slide Frame with authentic Python code
        create_scene_frame(
            lang=lang,
            chapter_slug=chapter_slug,
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
