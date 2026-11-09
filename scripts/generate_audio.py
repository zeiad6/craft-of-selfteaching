"""Generate narration audio and subtitles from the video scripts using Edge-TTS.

Usage:
    pip install edge-tts
    python scripts/generate_audio.py --lang ar                    # all chapters, Arabic
    python scripts/generate_audio.py --lang en --only 01-getting-started
    python scripts/generate_audio.py --lang ar --dry-run          # just print the text per scene

Output (git-ignored): videos/output/<lang>/<chapter>/scene-NN.mp3 and scene-NN.vtt
"""
import argparse
import asyncio
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "videos"
VOICES = {"ar": "ar-SA-HamedNeural", "en": "en-US-AriaNeural"}
AUDIO_RE = re.compile(r"^\*\*[^*]*Audio[^*]*:\*\*\s*(.+)$")


def read_scenes(md_file: Path) -> list[str]:
    """Return the Audio text of every scene in a script file."""
    scenes = []
    for line in md_file.read_text(encoding="utf-8").splitlines():
        match = AUDIO_RE.match(line.strip())
        if match:
            scenes.append(match.group(1).strip())
    return scenes


async def synthesize(text: str, voice: str, rate: str, mp3: Path, vtt: Path) -> None:
    import edge_tts

    communicate = edge_tts.Communicate(text, voice, rate=rate)
    submaker = edge_tts.SubMaker()
    with mp3.open("wb") as audio:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                submaker.feed(chunk)
    vtt.write_text(submaker.get_srt(), encoding="utf-8")


async def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lang", choices=VOICES, required=True)
    parser.add_argument("--only", help="chapter file stem, e.g. 05-functions")
    parser.add_argument("--voice", help="override the default voice")
    parser.add_argument("--rate", default="+0%", help='speech rate, e.g. "-10%%" for slower')
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    voice = args.voice or VOICES[args.lang]
    for md_file in sorted((ROOT / args.lang).glob("*.md")):
        if args.only and md_file.stem != args.only:
            continue
        out_dir = ROOT / "output" / args.lang / md_file.stem
        out_dir.mkdir(parents=True, exist_ok=True)
        for number, text in enumerate(read_scenes(md_file), 1):
            name = f"scene-{number:02d}"
            if args.dry_run:
                print(f"[{md_file.stem}/{name}] {text}")
                continue
            print(f"Generating {md_file.stem}/{name} ...")
            await synthesize(text, voice, args.rate, out_dir / f"{name}.mp3", out_dir / f"{name}.srt")


if __name__ == "__main__":
    asyncio.run(main())
