<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل السادس: النصوص والتعابير النمطية (Strings & Regex)

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الاستيرادات المشتركة

```python
import re
```

## 🟢 التحدي 1

```python
print(sum(ch in "aeiou" for ch in "Self teaching is a craft".lower()))
```

## 🟡 التحدي 2

```python
print(sum(int(n) for n in re.findall(r"\d+", "10 apples, 25 pears and 7 figs")))
```

## 🔴 التحدي 3

```python
strong = re.compile(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}")
for pw in ["weak", "Password1", "alllowercase1"]:
    print(pw, bool(strong.fullmatch(pw)))
```

---
[⬅️ العودة إلى الفصل](../../part-1-foundations/06-strings-and-regex.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
