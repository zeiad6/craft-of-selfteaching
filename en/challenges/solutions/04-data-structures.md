# 🔑 Reference Solutions: Chapter 4: Core Data Structures

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## Shared imports

```python
from collections import Counter, defaultdict
```

## 🟢 Challenge 1

```python
print(list(dict.fromkeys([3, 1, 3, 2, 1])))
```

## 🟡 Challenge 2

```python
sentence = "the quick brown fox jumps over the lazy dog the end"
counts = Counter(sentence.split())
print(counts.most_common(1))
```

## 🔴 Challenge 3

```python
original = {"a": 1, "b": 2, "c": 1}
inverted = defaultdict(list)
for key, value in original.items():
    inverted[value].append(key)
print(dict(inverted))
```

---
[⬅️ Back to the chapter](../../part-1-foundations/04-data-structures.ipynb) | [🏠 Challenges bank](../README.md)
