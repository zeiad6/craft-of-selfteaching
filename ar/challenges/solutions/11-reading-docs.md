<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل الحادي عشر: كيف تقرأ التوثيق الرسمي (Official Documentation)؟

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الحلول

```python
import textwrap
from itertools import pairwise

print("42".zfill(5))
print(textwrap.shorten("Self-teaching is the craft behind every craft", width=20, placeholder="..."))
nums = [1, 4, 9, 16, 25]
print([b - a for a, b in pairwise(nums)])
```

---
[⬅️ العودة إلى الفصل](../../part-3-mastery/11-reading-docs.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
