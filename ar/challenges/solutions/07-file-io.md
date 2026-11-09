<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل السابع: التعامل مع الملفات (File I/O)

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الاستيرادات المشتركة

```python
from collections import Counter
```

## 🟢 التحدي 1

```python
f1 = workdir / "five.txt"
f1.write_text("\n".join(f"line {i}" for i in range(1, 6)), encoding="utf-8")
print(len(f1.read_text(encoding="utf-8").splitlines()))
```

## 🟡 التحدي 2

```python
words = "to be or not to be".split()
freq = workdir / "freq.json"
freq.write_text(json.dumps(Counter(words)), encoding="utf-8")
print(freq.read_text(encoding="utf-8"))
```

## 🔴 التحدي 3

```python
def find_files(root: Path, suffix: str) -> list[Path]:
    return sorted(root.rglob(f"*{suffix}"))


print([p.name for p in find_files(workdir, ".json")])
```

---
[⬅️ العودة إلى الفصل](../../part-2-practice/07-file-io.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
