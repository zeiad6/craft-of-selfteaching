# 🎬 Video Production & Master Series | سيناريوهات وإنتاج الفيديوهات الشارحة

<div dir="rtl">

يوفر هذا المجلد مسار إنتاج متكامل وسلسلة فيديوهات مرئية شارحة كاملة (30 فيديو MP4 بدقة 1080p عالية الوضوح):

- **سيناريوهات الفيديوهات:** متوفرة بنسختين كاملتين في [`ar/`](./ar) و[`en/`](./en).
- **محرك الإنتاج الآلي:** أداة برمجية ذكية لتوليد الفيديوهات بصيغة **MP4** مباشرة مع الصوت والترجمة والإطارات التفاعلية.
- **الفيديوهات المكتملة:** 30 ملف فيديو متاح للمشاهدة والتشغيل المباشر في المستودع في [`rendered/`](./rendered).

---

## 🍿 المشاهدة المباشرة في المستودع (In-Repo Video Streaming)

يمكنك الآن مشاهدة جميع الفيديوهات الـ 30 مباشرة دون مغادرة المستودع:
- **استوديو المشاهدة المدمج (Interactive Web Player):** افتح صفحة **[ideos/index.html](./index.html)** (أو **[player.html](../player.html)**) لتجربة مشغل ويب متكامل مع قوائم التشغيل، والتحكم بالسرعة، والبحث اللحظي.
- **مشغل GitHub المباشر (Native GitHub Player):** بالنقر على أي رابط فيديو في الجدول أدناه يفتح الفيديو مباشرة داخل مشغل GitHub.
- **مشغل داخل الدفاتر التفاعلية (Jupyter & Colab):** كل دفتر في /ar و /en مزوّد بشارة تشغيل ومشغل مدمج لمتابعة الفيديو أثناء التدريب.

---

## ⚡ 1. الإنتاج والتوليد الآلي للفيديوهات (Automated MP4 Generation)

تم بناء أداة متطورة [`scripts/render_videos.py`](../scripts/render_videos.py) تجمع بين محرك **Edge-TTS** الصوتي ومحرك **FFmpeg** و **Pillow** لإنتاج الفيديوهات بصيغة MP4 جاهزة فوراً للنشر:

```bash
# تثبيت المتطلبات الإضافية (مرة واحدة)
pip install edge-tts imageio-ffmpeg pillow arabic-reshaper python-bidi

# توليد فيديو لفصل محدد (باللغة العربية)
python scripts/render_videos.py --lang ar --chapter 00-preface
python scripts/render_videos.py --lang ar --chapter 01-getting-started

# توليد كافة الفيديوهات الـ 30 دفعة واحدة
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

# Render all 30 chapters and appendices in bulk
python scripts/batch_render_all.py
```

📂 **Output:** Final assembled MP4 files are placed under `videos/rendered/` (e.g. `en_00-preface.mp4`).

---

## 🍿 صالة العرض والمشاهدة المباشرة في المستودع (Native In-Repo Video Theater)

يمكنك مشاهدة أي فيديو مباشرة هنا على GitHub بنقرة واحدة:

### 🇸🇦 الفيديوهات باللغة العربية (15 فيديو)

<details>
<summary><b>▶️ المقدمة: فلسفة التعلّم الذاتي كحرفة حياة (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/13d62d86-aabf-47a9-8c4d-df52f1fb8dfe

</details>
<details>
<summary><b>▶️ الفصل 01: الانطلاقة الأولى والقراءة الدقيقة (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/2320d37b-7123-42eb-8dcb-5064528994d5

</details>
<details>
<summary><b>▶️ الفصل 02: القيم والمتغيرات والمعاملات (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/844499a7-3e09-4d16-818a-487b83bc6bb8

</details>
<details>
<summary><b>▶️ الفصل 03: التحكم في التدفق ومطابقة الأنماط (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/d569e9e3-8667-49a7-8b66-6cb45d4e3471

</details>
<details>
<summary><b>▶️ الفصل 04: هياكل البيانات والقوائم والقواميس (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/90c34fd7-0709-4937-aa4e-c16767954c33

</details>
<details>
<summary><b>▶️ الفصل 05: الدوال وتفكيك المشكلات والمولدات (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/0539d6ce-6231-4ea8-9a6f-b36b37696800

</details>
<details>
<summary><b>▶️ الفصل 06: النصوص والتنسيق والتعابير النمطية (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/91c0a937-965e-4209-a7ef-59786762e001

</details>
<details>
<summary><b>▶️ الفصل 07: التعامل مع الملفات واستدامة البيانات (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/17ff9516-9fee-4da0-b42c-542ca46c1c9f

</details>
<details>
<summary><b>▶️ الفصل 08: البرمجة كائنية التوجه وفئات البيانات (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/570dd092-0fe5-49d7-8fdc-8d3f9b9617e3

</details>
<details>
<summary><b>▶️ الفصل 09: الوحدات البرمجية والبيئات المعزولة (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/795e86b1-abcd-4f9b-ae49-7f132faf5a72

</details>
<details>
<summary><b>▶️ الفصل 10: الاختبارات التلقائية والتنقيح (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/bc312277-b394-47ba-a7ea-164e6aec6426

</details>
<details>
<summary><b>▶️ الفصل 11: قراءة التوثيق الرسمي باحتراف (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/0cf82040-db9f-4d90-826e-78ec26284c9d

</details>
<details>
<summary><b>▶️ الفصل 12: بناء المشاريع الحقيقية والانطلاق (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/acb71d47-9d21-45bb-b3dd-3d68c7276649

</details>
<details>
<summary><b>▶️ الملحق أ: إعداد بيئة التطوير الحديثة (VS Code) (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/4ce1e587-ea6a-4580-bc5a-df3802b25c10

</details>
<details>
<summary><b>▶️ الملحق ب: أساسيات Git و GitHub للمتعلم الذاتي (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/28606c90-133c-412e-8b98-03806acded11

</details>

### 🌐 English Explainer Videos (15 Videos)

<details>
<summary><b>▶️ Preface: Self-Teaching as a Lifelong Craft (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/d671c5c7-92d9-4447-a301-f1bb7026714b

</details>
<details>
<summary><b>▶️ Chapter 01: Getting Started & Careful Reading (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/e1e6568e-974b-4051-bfd7-667e50421cd4

</details>
<details>
<summary><b>▶️ Chapter 02: Values, Variables, and Operators (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/ff0d9f7f-08ee-4e7d-afcf-d41d2b807525

</details>
<details>
<summary><b>▶️ Chapter 03: Control Flow & Pattern Matching (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/96da15ba-e403-4e02-98e2-993e0e844818

</details>
<details>
<summary><b>▶️ Chapter 04: Core Data Structures & Comprehensions (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/4b584012-e1f9-4382-a5cc-c5c26ceda59b

</details>
<details>
<summary><b>▶️ Chapter 05: Functions, Decomposition & Generators (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/f8b7f3f8-9085-4c06-9372-61bc58128348

</details>
<details>
<summary><b>▶️ Chapter 06: Strings, Formatting, and Regex (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/0ea108de-9f00-4c1e-ab43-baae501aa703

</details>
<details>
<summary><b>▶️ Chapter 07: File I/O & Data Persistence (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/4354269a-6545-40ea-9234-0d586976a16c

</details>
<details>
<summary><b>▶️ Chapter 08: Object-Oriented Programming & Dataclasses (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/7cb0140a-9e9a-4c67-b6d3-cdf9daebd6ed

</details>
<details>
<summary><b>▶️ Chapter 09: Modules, Packages, and Environments (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/22ea2c5b-380f-4134-9eb2-a1169ce2fcfc

</details>
<details>
<summary><b>▶️ Chapter 10: Debugging, Exceptions & Testing (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/f4f756c9-53ed-4fe7-9af2-40fcb2b0d3ff

</details>
<details>
<summary><b>▶️ Chapter 11: How to Read Official Documentation (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/6467843e-344e-4267-b0f9-26582273de91

</details>
<details>
<summary><b>▶️ Chapter 12: Building Real Projects Beyond Basics (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/a04a6f8a-5e68-4f94-8763-c9ccbf5e8e93

</details>
<details>
<summary><b>▶️ Appendix A: Modern Development Setup (VS Code) (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/860c53e1-be0f-4cce-9211-2cb96f5ebdec

</details>
<details>
<summary><b>▶️ Appendix B: Git & GitHub Essentials for Self-Learners (1080p MP4)</b></summary>

https://github.com/user-attachments/assets/db802696-5321-41ee-98d0-df755f353100

</details>

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
