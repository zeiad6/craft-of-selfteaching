# 🔑 Reference Solutions: Chapter 11: How to Read Official Documentation

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## Solutions

```python
import textwrap
from itertools import pairwise

print("42".zfill(5))
print(textwrap.shorten("Self-teaching is the craft behind every craft", width=20, placeholder="..."))
nums = [1, 4, 9, 16, 25]
print([b - a for a, b in pairwise(nums)])
```

---
[⬅️ Back to the chapter](../../part-3-mastery/11-reading-docs.ipynb) | [🏠 Challenges bank](../README.md)
