"""Add direct in-repo video players and streaming links to all 26 notebooks.
"""
import glob
import json
import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def main():
    updated = 0
    for lang in ["ar", "en"]:
        nbs = sorted(glob.glob(f"{lang}/**/*.ipynb", recursive=True))
        for nb_path in nbs:
            slug = os.path.basename(nb_path).replace(".ipynb", "")
            vid_slug = "00-preface" if slug == "01-preface" else slug

            with open(nb_path, "r", encoding="utf-8") as f:
                nb = json.load(f)

            cell0 = nb["cells"][0]
            src = "".join(cell0["source"])

            if "Watch Video In Repo" in src or "مشاهدة_مباشرة_في_المستودع" in src:
                continue

            if lang == "ar":
                badge_line = (
                    f"[![Watch Video In Repo](https://img.shields.io/badge/🎬_فيديو_شارح_1080p-مشاهدة_مباشرة_في_المستودع-E11D48?logo=youtube&logoColor=white)]"
                    f"(https://github.com/zeiad6/craft-of-selfteaching/blob/main/videos/rendered/ar_{vid_slug}.mp4)\n"
                    f"[![Web Player](https://img.shields.io/badge/🍿_استوديو_المشاهدة-Web_Player-38bdf8)]"
                    f"(\"../../videos/index.html#video=ar_{vid_slug}\")\n"
                )
                details_block = (
                    f"\n<details>\n"
                    f"<summary><b>🎬 تشغيل الفيديو الشارح لهذا الفصل (1080p Full HD) مباشرة في المستودع</b></summary>\n"
                    f"<br/>\n\n"
                    f"> 💡 **خيارات المشاهدة المباشرة السريعة:**\n"
                    f"> - [▶️ فتح الفيديو بمشغل GitHub المباشر (Native GitHub Player)](https://github.com/zeiad6/craft-of-selfteaching/blob/main/videos/rendered/ar_{vid_slug}.mp4)\n"
                    f"> - [🍿 فتح في استوديو الفيديوهات المتكامل (Web Player)](../../videos/index.html#video=ar_{vid_slug})\n"
                    f"> - [⬇️ تحميل ملف الفيديو بجودة 1080p](../../videos/rendered/ar_{vid_slug}.mp4)\n\n"
                    f"</details>\n"
                )
            else:
                badge_line = (
                    f"[![Watch Video In Repo](https://img.shields.io/badge/🎬_Watch_Video-Play_Directly_on_GitHub-E11D48?logo=youtube&logoColor=white)]"
                    f"(https://github.com/zeiad6/craft-of-selfteaching/blob/main/videos/rendered/en_{vid_slug}.mp4)\n"
                    f"[![Web Player](https://img.shields.io/badge/🍿_Video_Studio-Web_Player-38bdf8)]"
                    f"(\"../../videos/index.html#video=en_{vid_slug}\")\n"
                )
                details_block = (
                    f"\n<details>\n"
                    f"<summary><b>🎬 Watch the 1080p Explainer Video Directly in Repository</b></summary>\n"
                    f"<br/>\n\n"
                    f"> 💡 **Instant Streaming Options:**\n"
                    f"> - [▶️ Play Directly on GitHub Media Player](https://github.com/zeiad6/craft-of-selfteaching/blob/main/videos/rendered/en_{vid_slug}.mp4)\n"
                    f"> - [🍿 Open in Interactive Web Player](../../videos/index.html#video=en_{vid_slug})\n"
                    f"> - [⬇️ Download Master 1080p MP4](../../videos/rendered/en_{vid_slug}.mp4)\n\n"
                    f"</details>\n"
                )

            # Insert badge after Colab badge if present
            if "[![Open In Colab]" in src:
                parts = src.split(")\n", 1)
                new_src = parts[0] + ")\n" + badge_line + parts[1]
            else:
                new_src = badge_line + src

            new_src = new_src + details_block
            cell0["source"] = [line + "\n" for line in new_src.splitlines()]

            with open(nb_path, "w", encoding="utf-8") as f:
                json.dump(nb, f, ensure_ascii=False, indent=1)
                f.write("\n")

            updated += 1
            print(f"Updated: {nb_path}")

    print(f"✅ Successfully updated {updated} notebooks with direct in-repo video players!")

if __name__ == "__main__":
    main()
