# 🔑 Reference Solutions: Chapter 5: Functions & Problem Decomposition

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## Solutions

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
[⬅️ Back to the chapter](../../part-1-foundations/05-functions.ipynb) | [🏠 Challenges bank](../README.md)
