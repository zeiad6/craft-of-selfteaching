# 🔑 Reference Solutions: Chapter 9: Modules, Packages & The Python Ecosystem

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## Shared imports

```python
from collections import Counter
from datetime import date
import statistics
```

## 🟢 Challenge 1

```python
print((date(2027, 1, 1) - date.today()).days >= 0)
```

## 🟡 Challenge 2

```python
nums = [1, 2, 2, 3, 3, 3, 4]
print(Counter(nums).most_common(1)[0][0], statistics.mode(nums))
```

## 🔴 Challenge 3

```python
pkg = tmp / "mytools"
pkg.mkdir(exist_ok=True)
(pkg / "__init__.py").write_text("from .maths import double\n", encoding="utf-8")
(pkg / "maths.py").write_text("def double(x):\n    return x * 2\n", encoding="utf-8")
mytools = importlib.import_module("mytools")
print(mytools.double(21))
```

---
[⬅️ Back to the chapter](../../part-2-practice/09-modules.ipynb) | [🏠 Challenges bank](../README.md)
