<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل العاشر: الاختبارات ومعالجة الأخطاء (Debugging & Testing)

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الاستيرادات المشتركة

```python
import functools
```

## 🟢 التحدي 1

```python
def safe_div(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None


print(safe_div(6, 3), safe_div(1, 0))
```

## 🟡 التحدي 2

```python
def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    return cleaned == cleaned[::-1]


class TestPalindrome(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(is_palindrome("Never odd or even"))
        self.assertFalse(is_palindrome("python"))


print(unittest.TextTestRunner().run(
    unittest.defaultTestLoader.loadTestsFromTestCase(TestPalindrome)).wasSuccessful())
```

## 🔴 التحدي 3

```python
def retry(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    print(f"attempt {attempt} failed: {exc}")
                    if attempt == times:
                        raise
        return wrapper
    return decorator


calls = {"n": 0}


@retry(times=3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise RuntimeError("temporary failure")
    return "success"


print(flaky())
```

---
[⬅️ العودة إلى الفصل](../../part-2-practice/10-debugging-and-testing.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
