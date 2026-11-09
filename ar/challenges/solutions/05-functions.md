<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل الخامس: الدوال وتفكيك المشكلات (Functions)

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الحلول

```python
from itertools import islice


def is_even(n: int) -> bool:
    return n % 2 == 0


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    return cleaned == cleaned[::-1]


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(is_even(10), is_even(7))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Never odd or even"))
print(list(islice(fibonacci(), 10)))
```

---
[⬅️ العودة إلى الفصل](../../part-1-foundations/05-functions.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
