<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل الرابع: هياكل البيانات الأساسية (Data Structures)

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الاستيرادات المشتركة

```python
from collections import Counter, defaultdict
```

## 🟢 التحدي 1

```python
print(list(dict.fromkeys([3, 1, 3, 2, 1])))
```

## 🟡 التحدي 2

```python
sentence = "the quick brown fox jumps over the lazy dog the end"
counts = Counter(sentence.split())
print(counts.most_common(1))
```

## 🔴 التحدي 3

```python
original = {"a": 1, "b": 2, "c": 1}
inverted = defaultdict(list)
for key, value in original.items():
    inverted[value].append(key)
print(dict(inverted))
```

---
[⬅️ العودة إلى الفصل](../../part-1-foundations/04-data-structures.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
