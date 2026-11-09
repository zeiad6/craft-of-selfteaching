# 🔑 Reference Solutions: Chapter 12: Building Real Projects & Moving Beyond the Basics

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## 🟢 Challenge 1

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
[⬅️ Back to the chapter](../../part-3-mastery/12-beyond-basics.ipynb) | [🏠 Challenges bank](../README.md)
