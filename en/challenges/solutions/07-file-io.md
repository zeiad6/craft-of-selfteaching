# 🔑 Reference Solutions: Chapter 7: File I/O & Data Persistence

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## Shared imports

```python
from collections import Counter
```

## 🟢 Challenge 1

```python
f1 = workdir / "five.txt"
f1.write_text("\n".join(f"line {i}" for i in range(1, 6)), encoding="utf-8")
print(len(f1.read_text(encoding="utf-8").splitlines()))
```

## 🟡 Challenge 2

```python
words = "to be or not to be".split()
freq = workdir / "freq.json"
freq.write_text(json.dumps(Counter(words)), encoding="utf-8")
print(freq.read_text(encoding="utf-8"))
```

## 🔴 Challenge 3

```python
def find_files(root: Path, suffix: str) -> list[Path]:
    return sorted(root.rglob(f"*{suffix}"))


print([p.name for p in find_files(workdir, ".json")])
```

---
[⬅️ Back to the chapter](../../part-2-practice/07-file-io.ipynb) | [🏠 Challenges bank](../README.md)
