# 🎬 Video Production & Master Series | سيناريوهات وإنتاج الفيديوهات الشارحة

<div dir="rtl">

يوفر هذا المجلد مسار إنتاج متكامل وسلسلة فيديوهات مرئية شارحة كاملة (26 فيديو MP4 بدقة 1080p عالية الوضوح):

- **سيناريوهات الفيديوهات:** متوفرة بنسختين كاملتين في [`ar/`](./ar) و[`en/`](./en).
- **محرك الإنتاج الآلي:** أداة برمجية ذكية لتوليد الفيديوهات بصيغة **MP4** مباشرة مع الصوت والترجمة والإطارات التفاعلية.
- **الفيديوهات المكتملة:** 26 ملف فيديو متاح للمشاهدة والتحميل المباشر في [`rendered/`](./rendered).

---

## ⚡ 1. الإنتاج والتوليد الآلي للفيديوهات (Automated MP4 Generation)

تم بناء أداة متطورة [`scripts/render_videos.py`](../scripts/render_videos.py) تجمع بين محرك **Edge-TTS** الصوتي ومحرك **FFmpeg** و **Pillow** لإنتاج الفيديوهات بصيغة MP4 جاهزة فوراً للنشر:

```bash
# تثبيت المتطلبات الإضافية (مرة واحدة)
pip install edge-tts imageio-ffmpeg pillow arabic-reshaper python-bidi

# توليد فيديو لفصل محدد (باللغة العربية)
python scripts/render_videos.py --lang ar --chapter 00-preface
python scripts/render_videos.py --lang ar --chapter 01-getting-started

# توليد كافة الفصول الـ 26 دفعة واحدة
python scripts/batch_render_all.py
```

📂 **المخرجات:** يتم تصدير الفيديوهات النهائية المدمجة داخل المجلد `videos/rendered/` بدقة 1080p وحجم خفيف ومتوافق مع كافة المنصات.

---

## 🛠️ 2. الإنتاج اليدوي المخصص (CapCut Workflow)

إذا رغبت في إضافة مؤثرات بصرية مخصصة أو تسجيلات شاشة يدوية:
1. **توليد ملفات الصوت والترجمة:**
   ```bash
   python scripts/generate_audio.py --lang ar --only 00-preface
   ```
   الناتج: ملفات `scene-NN.mp3` مع ملفات الترجمة الزمنية `scene-NN.srt`.
2. **التجميع في CapCut:** أنشئ مشروعاً جديداً، وأسقط ملفات `.mp3` بالترتيب على مسار الصوت.
3. **الترجمة التلقائية:** استورد ملفات `.srt` عبر قائمة **Captions ← Import captions**.
4. **التصدير:** 1080p بصيغة MP4.

</div>

---

## ⚡ 1. Automated MP4 Generation Pipeline

We provide a zero-effort rendering engine [`scripts/render_videos.py`](../scripts/render_videos.py) combining **Edge-TTS**, **FFmpeg**, and **Pillow** to produce ready-to-publish 1080p MP4 videos:

```bash
# Install video rendering dependencies (once)
pip install edge-tts imageio-ffmpeg pillow arabic-reshaper python-bidi

# Render a specific chapter (English)
python scripts/render_videos.py --lang en --chapter 00-preface
python scripts/render_videos.py --lang en --chapter 01-getting-started

# Render all 26 chapters in bulk
python scripts/batch_render_all.py
```

📂 **Output:** Final assembled MP4 files are placed under `videos/rendered/` (e.g. `en_00-preface.mp4`).

---

## 📚 Complete Video Catalog | دليل الفيديوهات الشارحة الكامل (30/30 Ready)

| # | Chapter | 🇸🇦 سيناريو العربية | 🌐 English Script | 🎥 فيديو العربية (MP4) | 🎥 English Video (MP4) |
| :-: | :-- | :-: | :-: | :-- | :-- |
| 00 | Preface (المقدمة) | [ar](./ar/00-preface.md) | [en](./en/00-preface.md) | [▶️ ar_00-preface.mp4](./rendered/ar_00-preface.mp4) | [▶️ en_00-preface.mp4](./rendered/en_00-preface.mp4) |
| 01 | Getting Started (الانطلاقة الأولى) | [ar](./ar/01-getting-started.md) | [en](./en/01-getting-started.md) | [▶️ ar_01-getting-started.mp4](./rendered/ar_01-getting-started.mp4) | [▶️ en_01-getting-started.mp4](./rendered/en_01-getting-started.mp4) |
| 02 | Values & Operators (القيم والمعاملات) | [ar](./ar/02-values-and-operators.md) | [en](./en/02-values-and-operators.md) | [▶️ ar_02-values-and-operators.mp4](./rendered/ar_02-values-and-operators.mp4) | [▶️ en_02-values-and-operators.mp4](./rendered/en_02-values-and-operators.mp4) |
| 03 | Control Flow (التحكم في التدفق) | [ar](./ar/03-control-flow.md) | [en](./en/03-control-flow.md) | [▶️ ar_03-control-flow.mp4](./rendered/ar_03-control-flow.mp4) | [▶️ en_03-control-flow.mp4](./rendered/en_03-control-flow.mp4) |
| 04 | Data Structures (هياكل البيانات) | [ar](./ar/04-data-structures.md) | [en](./en/04-data-structures.md) | [▶️ ar_04-data-structures.mp4](./rendered/ar_04-data-structures.mp4) | [▶️ en_04-data-structures.mp4](./rendered/en_04-data-structures.mp4) |
| 05 | Functions (الدوال وتفكيك المشكلات) | [ar](./ar/05-functions.md) | [en](./en/05-functions.md) | [▶️ ar_05-functions.mp4](./rendered/ar_05-functions.mp4) | [▶️ en_05-functions.mp4](./rendered/en_05-functions.mp4) |
| 06 | Strings & Regex (النصوص والأنماط) | [ar](./ar/06-strings-and-regex.md) | [en](./en/06-strings-and-regex.md) | [▶️ ar_06-strings-and-regex.mp4](./rendered/ar_06-strings-and-regex.mp4) | [▶️ en_06-strings-and-regex.mp4](./rendered/en_06-strings-and-regex.mp4) |
| 07 | File I/O (الملفات واستدامة البيانات) | [ar](./ar/07-file-io.md) | [en](./en/07-file-io.md) | [▶️ ar_07-file-io.mp4](./rendered/ar_07-file-io.mp4) | [▶️ en_07-file-io.mp4](./rendered/en_07-file-io.mp4) |
| 08 | OOP (البرمجة كائنية التوجه) | [ar](./ar/08-oop.md) | [en](./en/08-oop.md) | [▶️ ar_08-oop.mp4](./rendered/ar_08-oop.mp4) | [▶️ en_08-oop.mp4](./rendered/en_08-oop.mp4) |
| 09 | Modules & Ecosystem (الوحدات والمكتبات) | [ar](./ar/09-modules.md) | [en](./en/09-modules.md) | [▶️ ar_09-modules.mp4](./rendered/ar_09-modules.mp4) | [▶️ en_09-modules.mp4](./rendered/en_09-modules.mp4) |
| 10 | Debugging & Testing (الاختبارات والأخطاء) | [ar](./ar/10-debugging-and-testing.md) | [en](./en/10-debugging-and-testing.md) | [▶️ ar_10-debugging-and-testing.mp4](./rendered/ar_10-debugging-and-testing.mp4) | [▶️ en_10-debugging-and-testing.mp4](./rendered/en_10-debugging-and-testing.mp4) |
| 11 | Reading Docs (قراءة التوثيق الرسمي) | [ar](./ar/11-reading-docs.md) | [en](./en/11-reading-docs.md) | [▶️ ar_11-reading-docs.mp4](./rendered/ar_11-reading-docs.mp4) | [▶️ en_11-reading-docs.mp4](./rendered/en_11-reading-docs.mp4) |
| 12 | Beyond Basics (بناء المشاريع الواقعية) | [ar](./ar/12-beyond-basics.md) | [en](./en/12-beyond-basics.md) | [▶️ ar_12-beyond-basics.mp4](./rendered/ar_12-beyond-basics.mp4) | [▶️ en_12-beyond-basics.mp4](./rendered/en_12-beyond-basics.mp4) |
| A | Appendix A: Setup (إعداد بيئة التطوير) | [ar](./ar/appendix-a-setup.md) | [en](./en/appendix-a-setup.md) | [▶️ ar_appendix-a-setup.mp4](./rendered/ar_appendix-a-setup.mp4) | [▶️ en_appendix-a-setup.mp4](./rendered/en_appendix-a-setup.mp4) |
| B | Appendix B: Git Basics (أساسيات جيت) | [ar](./ar/appendix-b-git.md) | [en](./en/appendix-b-git.md) | [▶️ ar_appendix-b-git.mp4](./rendered/ar_appendix-b-git.mp4) | [▶️ en_appendix-b-git.mp4](./rendered/en_appendix-b-git.mp4) |
