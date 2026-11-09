# 🎬 Video Production & Scripts | سيناريوهات وإنتاج الفيديو

<div dir="rtl">

يوفر هذا المجلد مسار إنتاج متكامل للفيديوهات الشارحة لكل فصل (3–4 مشاهد بدقة 1080p عالية الوضوح):

- **سيناريوهات الفيديوهات:** متوفرة بنسختين كاملتين في [`ar/`](./ar) و[`en/`](./en).
- **محرك الإنتاج الآلي:** أداة برمجية لتوليد الفيديوهات بصيغة **MP4** مباشرة مع الصوت والترجمة والإطارات التفاعلية.

---

## ⚡ 1. الإنتاج والتوليد الآلي للفيديوهات (Automated MP4 Generation)

تم بناء أداة متطورة [`scripts/render_videos.py`](../scripts/render_videos.py) تجمع بين محرك **Edge-TTS** الصوتي عالي النقاء ومحرك **FFmpeg** و **Pillow** لإنتاج الفيديوهات بصيغة MP4 جاهزة فوراً للنشر:

```bash
# تثبيت المتطلبات الإضافية (مرة واحدة)
pip install edge-tts imageio-ffmpeg pillow arabic-reshaper python-bidi

# توليد فيديو لفصل محدد (باللغة العربية)
python scripts/render_videos.py --lang ar --chapter 00-preface
python scripts/render_videos.py --lang ar --chapter 01-getting-started

# توليد فيديو لفصل محدد (باللغة الإنجليزية)
python scripts/render_videos.py --lang en --chapter 00-preface
python scripts/render_videos.py --lang en --chapter 01-getting-started

# توليد كافة الفصول تلقائياً دفعة واحدة
python scripts/render_videos.py --lang ar --all
```

📂 **المخرجات:** يتم تصدير الفيديوهات النهائية المدمجة داخل المجلد `videos/rendered/` (مثال: `ar_00-preface.mp4`).

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

# Render all chapters in bulk
python scripts/render_videos.py --lang en --all
```

📂 **Output:** Final assembled MP4 files are placed under `videos/rendered/` (e.g. `en_00-preface.mp4`).

---

## 📚 Scripts Directory | فهرس السيناريوهات

| Chapter | 🇸🇦 النسخة العربية | 🌐 English Edition | Rendered MP4 Sample |
| :-- | :-- | :-- | :-- |
| Preface | [ar](./ar/00-preface.md) | [en](./en/00-preface.md) | `videos/rendered/*_00-preface.mp4` |
| 1 | [ar](./ar/01-getting-started.md) | [en](./en/01-getting-started.md) | `videos/rendered/*_01-getting-started.mp4` |
| 2 | [ar](./ar/02-values-and-operators.md) | [en](./en/02-values-and-operators.md) | Ready to render |
| 3 | [ar](./ar/03-control-flow.md) | [en](./en/03-control-flow.md) | Ready to render |
| 4 | [ar](./ar/04-data-structures.md) | [en](./en/04-data-structures.md) | Ready to render |
| 5 | [ar](./ar/05-functions.md) | [en](./en/05-functions.md) | Ready to render |
| 6 | [ar](./ar/06-strings-and-regex.md) | [en](./en/06-strings-and-regex.md) | Ready to render |
| 7 | [ar](./ar/07-file-io.md) | [en](./en/07-file-io.md) | Ready to render |
| 8 | [ar](./ar/08-oop.md) | [en](./en/08-oop.md) | Ready to render |
| 9 | [ar](./ar/09-modules.md) | [en](./en/09-modules.md) | Ready to render |
| 10 | [ar](./ar/10-debugging-and-testing.md) | [en](./en/10-debugging-and-testing.md) | Ready to render |
| 11 | [ar](./ar/11-reading-docs.md) | [en](./en/11-reading-docs.md) | Ready to render |
| 12 | [ar](./ar/12-beyond-basics.md) | [en](./en/12-beyond-basics.md) | Ready to render |
