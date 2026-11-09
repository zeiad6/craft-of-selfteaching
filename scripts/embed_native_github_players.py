"""Embed native GitHub inline video players into all 26 notebooks, README.md, and videos/README.md.
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

def update_notebooks(assets: dict[str, str]):
    updated = 0
    for lang in ["ar", "en"]:
        nbs = sorted(glob.glob(f"{lang}/**/*.ipynb", recursive=True))
        for nb_path in nbs:
            slug = os.path.basename(nb_path).replace(".ipynb", "")
            vid_slug = "00-preface" if slug == "01-preface" else slug
            asset_key = f"{lang}_{vid_slug}.mp4"
            asset_url = assets.get(asset_key)
            if not asset_url:
                continue

            with open(nb_path, "r", encoding="utf-8") as f:
                nb = json.load(f)

            cell0 = nb["cells"][0]
            src = "".join(cell0["source"])

            if lang == "ar":
                badge_line = (
                    f"[![Watch Video In Repo](https://img.shields.io/badge/🎬_فيديو_شارح_1080p-مشاهدة_مباشرة_في_المستودع-E11D48?logo=youtube&logoColor=white)]"
                    f"({asset_url})\n"
                    f"[![Web Player](https://img.shields.io/badge/🍿_استوديو_المشاهدة-Web_Player-38bdf8)]"
                    f"(\"../../videos/index.html#video=ar_{vid_slug}\")\n"
                )
                details_block = (
                    f"\n<details open>\n"
                    f"<summary><b>🎬 مشغل الفيديو المباشر داخل المستودع (1080p Full HD) — انقر للمشاهدة فوراً</b></summary>\n\n"
                    f"{asset_url}\n\n"
                    f"> 💡 **خيارات إضافية:** [🍿 استوديو المشاهدة المتكامل (Web Player)]"
                    f"(\"../../videos/index.html#video=ar_{vid_slug}\") • [⬇️ تحميل ملف الفيديو](../../videos/rendered/ar_{vid_slug}.mp4)\n\n"
                    f"</details>\n"
                )
            else:
                badge_line = (
                    f"[![Watch Video In Repo](https://img.shields.io/badge/🎬_Watch_Video-Play_Directly_on_GitHub-E11D48?logo=youtube&logoColor=white)]"
                    f"({asset_url})\n"
                    f"[![Web Player](https://img.shields.io/badge/🍿_Video_Studio-Web_Player-38bdf8)]"
                    f"(\"../../videos/index.html#video=en_{vid_slug}\")\n"
                )
                details_block = (
                    f"\n<details open>\n"
                    f"<summary><b>🎬 In-Repo Video Player (1080p Full HD) — Click to Stream Directly</b></summary>\n\n"
                    f"{asset_url}\n\n"
                    f"> 💡 **Additional Streaming Options:** [🍿 Interactive Web Player]"
                    f"(\"../../videos/index.html#video=en_{vid_slug}\") • [⬇️ Download Master MP4](../../videos/rendered/en_{vid_slug}.mp4)\n\n"
                    f"</details>\n"
                )

            # Strip old details block if any
            if "<details" in src:
                src = src.split("<details")[0].strip() + "\n"

            # Re-insert badge line
            if "[![Watch Video In Repo]" in src:
                lines = src.splitlines()
                filtered = [l for l in lines if not any(k in l for k in ["Watch Video In Repo", "Web Player"])]
                src = "\n".join(filtered) + "\n"

            if "[![Open In Colab]" in src:
                parts = src.split(")\n", 1)
                new_src = parts[0] + ")\n" + badge_line + parts[1]
            else:
                new_src = badge_line + src

            new_src = new_src + details_block
            cell0["source"] = [l + "\n" for l in new_src.splitlines()]

            with open(nb_path, "w", encoding="utf-8") as f:
                json.dump(nb, f, ensure_ascii=False, indent=1)
                f.write("\n")

            updated += 1
            print(f"Updated {nb_path} with native video player")

    print(f"✅ Successfully updated {updated} notebooks with native GitHub video players!")


def update_videos_readme(assets: dict[str, str]):
    path = "videos/README.md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Build collapsible players section for all 30 videos
    players_ar = []
    players_en = []

    titles_ar = {
        "00-preface": "المقدمة: فلسفة التعلّم الذاتي كحرفة حياة",
        "01-getting-started": "الفصل 01: الانطلاقة الأولى والقراءة الدقيقة",
        "02-values-and-operators": "الفصل 02: القيم والمتغيرات والمعاملات",
        "03-control-flow": "الفصل 03: التحكم في التدفق ومطابقة الأنماط",
        "04-data-structures": "الفصل 04: هياكل البيانات والقوائم والقواميس",
        "05-functions": "الفصل 05: الدوال وتفكيك المشكلات والمولدات",
        "06-strings-and-regex": "الفصل 06: النصوص والتنسيق والتعابير النمطية",
        "07-file-io": "الفصل 07: التعامل مع الملفات واستدامة البيانات",
        "08-oop": "الفصل 08: البرمجة كائنية التوجه وفئات البيانات",
        "09-modules": "الفصل 09: الوحدات البرمجية والبيئات المعزولة",
        "10-debugging-and-testing": "الفصل 10: الاختبارات التلقائية والتنقيح",
        "11-reading-docs": "الفصل 11: قراءة التوثيق الرسمي باحتراف",
        "12-beyond-basics": "الفصل 12: بناء المشاريع الحقيقية والانطلاق",
        "appendix-a-setup": "الملحق أ: إعداد بيئة التطوير الحديثة (VS Code)",
        "appendix-b-git": "الملحق ب: أساسيات Git و GitHub للمتعلم الذاتي"
    }

    titles_en = {
        "00-preface": "Preface: Self-Teaching as a Lifelong Craft",
        "01-getting-started": "Chapter 01: Getting Started & Careful Reading",
        "02-values-and-operators": "Chapter 02: Values, Variables, and Operators",
        "03-control-flow": "Chapter 03: Control Flow & Pattern Matching",
        "04-data-structures": "Chapter 04: Core Data Structures & Comprehensions",
        "05-functions": "Chapter 05: Functions, Decomposition & Generators",
        "06-strings-and-regex": "Chapter 06: Strings, Formatting, and Regex",
        "07-file-io": "Chapter 07: File I/O & Data Persistence",
        "08-oop": "Chapter 08: Object-Oriented Programming & Dataclasses",
        "09-modules": "Chapter 09: Modules, Packages, and Environments",
        "10-debugging-and-testing": "Chapter 10: Debugging, Exceptions & Testing",
        "11-reading-docs": "Chapter 11: How to Read Official Documentation",
        "12-beyond-basics": "Chapter 12: Building Real Projects Beyond Basics",
        "appendix-a-setup": "Appendix A: Modern Development Setup (VS Code)",
        "appendix-b-git": "Appendix B: Git & GitHub Essentials for Self-Learners"
    }

    for slug, title in titles_ar.items():
        key = f"ar_{slug}.mp4"
        url = assets.get(key, "")
        if url:
            players_ar.append(
                f"<details>\n"
                f"<summary><b>▶️ {title} (1080p MP4)</b></summary>\n\n"
                f"{url}\n\n"
                f"</details>\n"
            )

    for slug, title in titles_en.items():
        key = f"en_{slug}.mp4"
        url = assets.get(key, "")
        if url:
            players_en.append(
                f"<details>\n"
                f"<summary><b>▶️ {title} (1080p MP4)</b></summary>\n\n"
                f"{url}\n\n"
                f"</details>\n"
            )

    theater_section = (
        "## 🍿 صالة العرض والمشاهدة المباشرة في المستودع (Native In-Repo Video Theater)\n\n"
        "يمكنك مشاهدة أي فيديو مباشرة هنا على GitHub بنقرة واحدة:\n\n"
        "### 🇸🇦 الفيديوهات باللغة العربية (15 فيديو)\n\n"
        + "".join(players_ar)
        + "\n### 🌐 English Explainer Videos (15 Videos)\n\n"
        + "".join(players_en)
        + "\n---\n\n"
    )

    if "## 🍿 صالة العرض والمشاهدة المباشرة" in text:
        parts = text.split("## 🍿 صالة العرض والمشاهدة المباشرة")
        tail = parts[1].split("\n---\n\n", 1)[1] if "\n---\n\n" in parts[1] else parts[1]
        text = parts[0] + theater_section + tail
    else:
        text = text.replace("## 📚 Complete Video Catalog", theater_section + "## 📚 Complete Video Catalog")

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print("✅ Successfully updated videos/README.md with native player embeds!")


def update_root_readme(assets: dict[str, str]):
    path = "README.md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Update table links to use the exact asset URLs directly!
    for key, url in assets.items():
        # ar_01-getting-started.mp4
        old_pattern = f"https://github.com/zeiad6/craft-of-selfteaching/blob/main/videos/rendered/{key}"
        text = text.replace(old_pattern, url)

    # Add featured direct player section in README.md
    featured_players = (
        "### 🍿 صالة المشاهدة المباشرة داخل المستودع (In-Repo Native Video Player)\n\n"
        "اضغط على أي فصل لمشاهدة الفيديو الشارح فوراً داخل واجهة GitHub دون مغادرة الصفحة:\n\n"
        "<details open>\n"
        "<summary><b>🎬 شاهد فيديو المقدمة: فلسفة التعلّم الذاتي (Preface 1080p)</b></summary>\n\n"
        f"{assets['ar_00-preface.mp4']}\n\n"
        "</details>\n\n"
        "<details>\n"
        "<summary><b>🎬 شاهد فيديو الفصل 01: الانطلاقة الأولى والقراءة الدقيقة (Getting Started)</b></summary>\n\n"
        f"{assets['ar_01-getting-started.mp4']}\n\n"
        "</details>\n\n"
        "<details>\n"
        "<summary><b>🎬 شاهد فيديو الفصل 03: التحكم في التدفق ومطابقة الأنماط (Control Flow & Match/Case)</b></summary>\n\n"
        f"{assets['ar_03-control-flow.mp4']}\n\n"
        "</details>\n\n"
        f"> 💡 **لمشاهدة كافة الفيديوهات الـ 30 مباشرة:** تفضل بزيارة **[صالة العرض الكاملة (videos/README.md)](./videos/README.md)** أو افتح **[استوديو المشاهدة التفاعلي (videos/index.html)](./videos/index.html)**.\n\n"
    )

    if "### 🍿 صالة المشاهدة المباشرة داخل المستودع" in text:
        parts = text.split("### 🍿 صالة المشاهدة المباشرة داخل المستودع")
        tail = parts[1].split("\n---\n", 1)[1] if "\n---\n" in parts[1] else parts[1]
        text = parts[0] + featured_players + "---\n" + tail
    else:
        # Insert before section ⚡ خيارات التشغيل التفاعلي
        target = "## ⚡ خيارات التشغيل التفاعلي"
        text = text.replace(target, featured_players + "---\n\n" + target)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print("✅ Successfully updated README.md with native GitHub video players!")


def main():
    with open("videos/github_video_assets.json", "r", encoding="utf-8") as f:
        assets = json.load(f)

    update_notebooks(assets)
    update_videos_readme(assets)
    update_root_readme(assets)

if __name__ == "__main__":
    main()
