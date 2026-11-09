"""Batch render all 26 chapter videos (Arabic & English) with the upgraded UI/UX design.

Usage:
  python scripts/batch_render_all.py
"""
import asyncio
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from render_videos import render_chapter, VIDEOS_DIR, OUTPUT_DIR

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


async def main():
    start_time = time.time()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    tasks = []
    for lang in ["ar", "en"]:
        scripts = sorted((VIDEOS_DIR / lang).glob("*.md"))
        for s in scripts:
            tasks.append((lang, s.stem))

    total = len(tasks)
    print(f"🚀 Starting full video generation for all {total} chapters...")

    success_count = 0
    for idx, (lang, slug) in enumerate(tasks, 1):
        target_file = OUTPUT_DIR / f"{lang}_{slug}.mp4"
        print(f"\n==================================================")
        print(f"[{idx}/{total}] Processing: {lang.upper()} -> {slug}")
        print(f"==================================================")
        try:
            res = await render_chapter(lang, slug)
            if res and res.exists():
                success_count += 1
                mb = res.stat().st_size / (1024 * 1024)
                print(f"🎉 Completed [{idx}/{total}]: {res.name} ({mb:.2f} MB)")
        except Exception as e:
            print(f"⚠️ Error rendering {lang}_{slug}: {e}")

    elapsed = time.time() - start_time
    print(f"\n🏁 Finished rendering: {success_count}/{total} videos generated in {elapsed / 60:.1f} minutes!")


if __name__ == "__main__":
    asyncio.run(main())
