<div dir="rtl">

# 📎 الملحق ب: أساسيات Git و GitHub للمتعلم الذاتي

**Git** نظام لحفظ تاريخ مشروعك، و**GitHub** منصة لاستضافته ومشاركته. وجود مستودع عام بمشاريعك هو أفضل سيرة ذاتية لمتعلم ذاتي.

## 1. الإعداد لمرة واحدة
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

## 2. دورة العمل الأساسية
```bash
git init                      # إنشاء مستودع جديد
git status                    # ماذا تغيّر؟
git add .                     # تجهيز التعديلات
git commit -m "Add chapter 1" # حفظ لقطة
git log --oneline             # عرض التاريخ
```

## 3. النشر على GitHub
1. أنشئ مستودعاً فارغاً على GitHub (**Public**).
2. اربطه وارفع الكود:
```bash
git remote add origin https://github.com/zeiad6/craft-of-selfteaching.git
git branch -M main
git push -u origin main
```

## 4. الفروع و Pull Requests
```bash
git switch -c feat/new-challenge   # فرع جديد
# ... عدّل وسجّل ...
git push -u origin feat/new-challenge
```
ثم افتح **Pull Request** من صفحة المستودع. نصائح: اجعل كل فرع لمهمة واحدة، واكتب رسائل `commit` واضحة بصيغة الأمر (`Fix typo in chapter 3`).

## 5. ملف `.gitignore`
لا ترفع البيئة الافتراضية ولا الأسرار:
```text
.venv/
__pycache__/
.ipynb_checkpoints/
.env
```

> [!WARNING]
> لا تضع كلمات المرور أو مفاتيح API داخل المستودع أبداً. إن رفعتها بالخطأ فاعتبرها مكشوفة وغيّرها فوراً.

## 6. أخطاء شائعة
| الموقف | الحل |
| :-- | :-- |
| تراجع عن تعديل غير محفوظ في ملف | `git restore file.py` |
| إلغاء `git add` | `git restore --staged file.py` |
| تعديل آخر رسالة commit | `git commit --amend` |

---
[➡️ الملحق أ](./01-setup-environment.md) | [🏠 الفهرس العربي](../README.md) | [💡 بنك التحديات ⬅️](../challenges/README.md)

</div>
