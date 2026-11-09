# 🤝 دليل المساهمة | Contribution Guidelines

<div dir="rtl">

شكراً لاهتمامك بالمساهمة في مشروع **"فن التعلّم الذاتي" (The Craft of Self-Teaching)**! هذا المشروع يهدف لتقديم مرجع عالمي باللغتين العربية والإنجليزية لتعلّم البرمجة ومهارة التعلّم الذاتي باستخدام أحدث إصدارات **Python 3.12+**.

## 🌟 كيف يمكنك المساهمة؟

1. **تحسين الترجمة والصياغة (Localization):**
   - تصحيح الأخطاء الإملائية أو النحوية في النسختين العربية (`/ar`) أو الإنجليزية (`/en`).
   - اقتراح مصطلحات تقنية عربية أدق مع الحفاظ على المصطلح الإنجليزي بين قوسين عند أول ذكر له.
2. **تحديث الأكواد (Python 3.12+ Modernization):**
   - تحسين أمثلة الكود لتتبع أفضل الممارسات الحديثة (PEP 8، Type Hints، f-strings).
   - التأكد من خلو جميع دفاتر Jupyter (`.ipynb`) من أي أخطاء برمجية.
3. **إثراء بنك التحديات البرمجية (Coding Challenges):**
   - إضافة تمارين وتحديات جديدة في نهاية الفصول أو داخل مجلد `challenges/` مع حلولها النموذجية المشروحة.

## 🛠️ خطوات إرسال مساهمتك (Pull Request Workflow)

1. قم بعمل **Fork** للمستودع إلى حسابك الشخصي.
2. أنشئ فرعاً جديداً (Branch) يصف التعديل:
   ```bash
   git checkout -b feat/add-chapter-1-challenges
   # أو لتصحيح لغوي:
   git checkout -b fix/ar-typo-preface
   ```
3. تأكد من تشغيل الخلايا البرمجية في Jupyter Notebook والتحقق من صحتها على **Python 3.12+**.
4. أرسل **Pull Request** مع وصف واضح للتغييرات التي قمت بها.

## 📐 معايير الترجمة والتعريب المعتمدة في المشروع
- **لا للترجمة الحرفية:** نترجم المعنى والروح التعليمية بأسلوب عربي فصيح، سلس، ومباشر.
- **المصطلحات التقنية:** نكتب المصطلح العربي متبوعاً بالمصطلح الإنجليزي بين قوسين عند ذكره لأول مرة في الفصل، مثل:
  - البرمجة كائنية التوجه (Object-Oriented Programming - OOP)
  - القوائم الإدراكية / المختصرة (List Comprehensions)
  - تلميحات الأنواع (Type Hints)
  - الدوال المجهولة (Lambda Functions)

</div>

---

## 🌐 Contributing (English)

Thank you for your interest in contributing to **The Craft of Self-Teaching**! Our goal is to maintain a world-class, bilingual (English & Arabic) interactive curriculum for self-learners using **Python 3.12+**.

### 🌟 Ways to Contribute
1. **Editorial & Translation Improvements:** Enhance clarity, fix typos, or refine explanations in `/en` or `/ar`.
2. **Python 3.12+ Code Modernization:** Ensure all code cells follow modern Python idioms (PEP 8, type annotations, modern standard library usage).
3. **New Coding Challenges:** Add practical exercises and reference solutions under `challenges/`.

### 🛠️ Pull Request Checklist
- [ ] Code cells run cleanly on **Python 3.12+**.
- [ ] Explanations are clear, beginner-friendly, and faithful to the self-teaching philosophy.
- [ ] If adding a structural change, both `/ar` and `/en` directories remain synchronized where applicable.
