"""Upload all rendered MP4 videos to GitHub user-attachments asset server.

This gives each video a permanent `https://github.com/user-attachments/assets/...`
URL which GitHub's Markdown parser automatically renders as an embedded,
in-line, native playable video player directly on GitHub without leaving the page.
"""
import glob
import json
import os
import sys
import time
import urllib.request
import urllib.error

TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO_ID = 1450903717
OUTPUT_JSON = "videos/github_video_assets.json"

def get_existing_assets() -> dict[str, str]:
    if os.path.exists(OUTPUT_JSON):
        try:
            with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_assets(assets: dict[str, str]):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(assets, f, indent=2, ensure_ascii=False)
        f.write("\n")

def upload_video(file_path: str) -> str | None:
    file_name = os.path.basename(file_path)
    url = f"https://uploads.github.com/user-attachments/assets?name={file_name}&content_type=video/mp4&repository_id={REPO_ID}"

    with open(file_path, "rb") as f:
        data = f.read()

    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/json",
            "User-Agent": "Craft-Of-Selfteaching-Uploader"
        },
        method="POST"
    )

    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                res = json.loads(resp.read().decode())
                asset_url = res.get("url") or res.get("href")
                return asset_url
        except urllib.error.HTTPError as e:
            print(f"  [Attempt {attempt}] HTTP Error {e.code}: {e.read().decode()[:200]}")
        except Exception as e:
            print(f"  [Attempt {attempt}] Error: {e}")
        time.sleep(2)
    return None

def main():
    videos = sorted(glob.glob("videos/rendered/*.mp4"))
    print(f"Found {len(videos)} videos to process...")

    assets = get_existing_assets()
    total = len(videos)

    for idx, v in enumerate(videos, 1):
        name = os.path.basename(v)
        if name in assets and assets[name]:
            print(f"[{idx}/{total}] Already uploaded: {name} -> {assets[name]}")
            continue

        size_mb = os.path.getsize(v) / (1024 * 1024)
        print(f"[{idx}/{total}] Uploading {name} ({size_mb:.2f} MB)...")
        asset_url = upload_video(v)
        if asset_url:
            assets[name] = asset_url
            save_assets(assets)
            print(f"  -> Success: {asset_url}")
        else:
            print(f"  -> Failed to upload {name}!")

    print(f"\nAll uploads completed! {len(assets)}/{total} assets recorded in {OUTPUT_JSON}.")

if __name__ == "__main__":
    main()
