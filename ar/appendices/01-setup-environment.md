<div dir="rtl">

# 📎 الملحق أ: إعداد بيئة العمل الحديثة (VS Code + JupyterLab + Python 3.12+)

## 1. تثبيت Python 3.12+
- **Windows:** حمّله من [python.org](https://www.python.org/downloads/) وفعّل خيار **Add python.exe to PATH**، أو استخدم `winget install Python.Python.3.12`.
- **macOS:** `brew install python@3.12`
- **Linux:** عبر مدير حزم التوزيعة أو `pyenv`.

تحقق من التثبيت:
```bash
python --version
```

## 2. البيئة الافتراضية وتثبيت المتطلبات
```bash
git clone https://github.com/zeiad6/craft-of-selfteaching.git
cd craft-of-selfteaching

# الطريقة الكلاسيكية
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
```

### بديل أسرع: `uv`
```bash
pip install uv
uv venv
uv pip install -r requirements.txt
```

## 3. VS Code
1. ثبّت [VS Code](https://code.visualstudio.com/).
2. ثبّت الإضافات: **Python** و**Jupyter** و**Pylance** (جميعها من Microsoft). ويُنصح بإضافة **Ruff** للتنسيق والفحص.
3. افتح المجلد، ثم اضغط `Ctrl+Shift+P` واختر **Python: Select Interpreter** وحدّد `.venv`.
4. افتح أي ملف `.ipynb` واختر النواة (Kernel) من أعلى اليمين، ثم شغّل الخلية بـ `Shift+Enter`.

اختصارات مفيدة: `Ctrl+Shift+P` لقائمة الأوامر، و`F5` للتشغيل مع التنقيح، و`F9` لوضع نقطة توقف.

## 4. JupyterLab
```bash
jupyter lab
```
- `Shift+Enter` تشغيل الخلية، و`Esc` ثم `A`/`B` إضافة خلية فوق/تحت، و`M` تحويلها لنص، و`Y` لكود.
- من **Kernel ← Restart Kernel and Run All Cells** تتأكد أن الدفتر يعمل كاملاً من الصفر.
- قائمة **View ← Show Table of Contents** تعرض فهرس الدفتر.

## 5. Google Colab (بدون تثبيت)
افتح الدفتر عبر زر **Open in Colab**. تعمل الأكواد في هذا الكتاب مباشرة، وتتوفر فيه عادة نسخة حديثة من بايثون. تحقق منها بـ:
```python
import sys; print(sys.version)
```

## 6. حل المشكلات الشائعة
| المشكلة | الحل |
| :-- | :-- |
| `python` غير معروف | أعد التثبيت مع إضافة PATH، أو جرّب `py` على Windows |
| تعذّر تفعيل `.venv` في PowerShell | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| لا تظهر النواة في VS Code | `pip install ipykernel` داخل البيئة الافتراضية |
| حروف عربية مشوّهة عند القراءة | مرّر `encoding="utf-8"` عند فتح الملفات |

---
[🏠 الفهرس العربي](../README.md) | [الملحق ب: Git و GitHub ⬅️](./02-git-basics.md)

</div>
