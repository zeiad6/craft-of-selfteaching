<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل التاسع: الوحدات والمكتبات (Modules & Packages)

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الاستيرادات المشتركة

```python
from collections import Counter
from datetime import date
import statistics
```

## 🟢 التحدي 1

```python
print((date(2027, 1, 1) - date.today()).days >= 0)
```

## 🟡 التحدي 2

```python
nums = [1, 2, 2, 3, 3, 3, 4]
print(Counter(nums).most_common(1)[0][0], statistics.mode(nums))
```

## 🔴 التحدي 3

```python
pkg = tmp / "mytools"
pkg.mkdir(exist_ok=True)
(pkg / "__init__.py").write_text("from .maths import double\n", encoding="utf-8")
(pkg / "maths.py").write_text("def double(x):\n    return x * 2\n", encoding="utf-8")
mytools = importlib.import_module("mytools")
print(mytools.double(21))
```

---
[⬅️ العودة إلى الفصل](../../part-2-practice/09-modules.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
