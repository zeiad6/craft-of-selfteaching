<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل الثاني عشر: بناء المشاريع الحقيقية وما بعد الأساسيات

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## 🟢 التحدي 1

```python
def clear_done(path: Path) -> int:
    tasks = load(path)
    remaining = [t for t in tasks if not t.done]
    save(path, remaining)
    return len(tasks) - len(remaining)


print("removed:", clear_done(store))
run(["list"], store)
```

---
[⬅️ العودة إلى الفصل](../../part-3-mastery/12-beyond-basics.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
