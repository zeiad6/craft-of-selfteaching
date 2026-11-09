# 🎬 Video Scripts | سيناريوهات الفيديو

<div dir="rtl">

لكل فصل سيناريو فيديو شارح قصير (3–4 مشاهد، دقيقتان تقريباً)، بنسختين: [`ar/`](./ar) و[`en/`](./en). كل مشهد يتكون من:

- **Visual:** ما يظهر على الشاشة (كود، رسم، نص).
- **Audio:** نص التعليق الصوتي، مكتوب بلا رموز برمجية ولا إيموجي ليقرأه Edge-TTS بشكل طبيعي. الكلمات البرمجية مثل `print` و`if` تبقى بالإنجليزية داخل النص العربي.

## ⚙️ خطوات الإنتاج المجاني

1. **توليد الصوت والترجمة النصية:**
   ```bash
   pip install edge-tts
   python scripts/generate_audio.py --lang ar                      # كل الفصول
   python scripts/generate_audio.py --lang en --only 05-functions  # فصل واحد
   python scripts/generate_audio.py --lang ar --dry-run            # عرض النصوص فقط
   ```
   الناتج في `videos/output/<lang>/<chapter>/` : ملف `scene-NN.mp3` وملف ترجمة `scene-NN.srt` لكل مشهد.
   الأصوات الافتراضية: `ar-SA-HamedNeural` و`en-US-AriaNeural`. لتجربة أصوات أخرى: `edge-tts --list-voices`، ثم `--voice <الاسم>`. ولتبطئ الكلام استخدم `--rate "-10%"`.
2. **التجميع في CapCut:** أنشئ مشروعاً جديداً، واستورد ملفات `.mp3` ثم رتّبها على المسار الصوتي بالترتيب. اضبط المشاهد المرئية حسب سطر **Visual**: التقط لقطات شاشة للأكواد من الدفاتر، أو سجّل شاشتك وأنت تشغّل الخلايا.
3. **الترجمة النصية:** استورد ملفات `.srt` عبر **Captions ← Import captions** في CapCut.
4. **التصدير:** 1080p، وانشر الفيديو مع رابط الفصل في وصفه.

> تنبيه: يحتاج `edge-tts` إلى اتصال بالإنترنت لأنه يستخدم خدمة Microsoft Edge للقراءة الصوتية. راجع شروط الاستخدام الخاصة بالخدمة وبـ CapCut قبل النشر التجاري.

</div>

---

Every chapter has a short explainer-video script (3–4 scenes, about two minutes) in [`en/`](./en) and [`ar/`](./ar). Each scene has:

- **Visual:** what appears on screen (code, diagrams, text).
- **Audio:** the narration text, written without code symbols or emoji so Edge-TTS reads it naturally.

## ⚙️ Free Production Workflow

1. **Generate narration and subtitles:**
   ```bash
   pip install edge-tts
   python scripts/generate_audio.py --lang en                      # all chapters
   python scripts/generate_audio.py --lang en --only 05-functions  # one chapter
   python scripts/generate_audio.py --lang en --dry-run            # print text only
   ```
   Output goes to `videos/output/<lang>/<chapter>/`: `scene-NN.mp3` plus `scene-NN.srt` per scene. Default voices are `en-US-AriaNeural` and `ar-SA-HamedNeural`; list others with `edge-tts --list-voices` and pass `--voice <name>`. Slow the pace with `--rate "-10%"`.
2. **Assemble in CapCut:** create a project, import the `.mp3` files and place them in order on the audio track. Build visuals from each scene's **Visual** line: screenshot the notebook code, or screen-record yourself running the cells.
3. **Subtitles:** import the `.srt` files via **Captions → Import captions**.
4. **Export:** 1080p, and link the chapter notebook in the video description.

> Note: `edge-tts` needs an internet connection because it uses Microsoft Edge's online speech service. Review the terms of that service and of CapCut before commercial use.

## 📚 Scripts

| Chapter | العربية | English |
| :-- | :-- | :-- |
| Preface | [ar](./ar/00-preface.md) | [en](./en/00-preface.md) |
| 1 | [ar](./ar/01-getting-started.md) | [en](./en/01-getting-started.md) |
| 2 | [ar](./ar/02-values-and-operators.md) | [en](./en/02-values-and-operators.md) |
| 3 | [ar](./ar/03-control-flow.md) | [en](./en/03-control-flow.md) |
| 4 | [ar](./ar/04-data-structures.md) | [en](./en/04-data-structures.md) |
| 5 | [ar](./ar/05-functions.md) | [en](./en/05-functions.md) |
| 6 | [ar](./ar/06-strings-and-regex.md) | [en](./en/06-strings-and-regex.md) |
| 7 | [ar](./ar/07-file-io.md) | [en](./en/07-file-io.md) |
| 8 | [ar](./ar/08-oop.md) | [en](./en/08-oop.md) |
| 9 | [ar](./ar/09-modules.md) | [en](./en/09-modules.md) |
| 10 | [ar](./ar/10-debugging-and-testing.md) | [en](./en/10-debugging-and-testing.md) |
| 11 | [ar](./ar/11-reading-docs.md) | [en](./en/11-reading-docs.md) |
| 12 | [ar](./ar/12-beyond-basics.md) | [en](./en/12-beyond-basics.md) |
