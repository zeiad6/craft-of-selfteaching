# 🔑 Reference Solutions: Chapter 6: Strings & Regular Expressions

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## Shared imports

```python
import re
```

## 🟢 Challenge 1

```python
print(sum(ch in "aeiou" for ch in "Self teaching is a craft".lower()))
```

## 🟡 Challenge 2

```python
print(sum(int(n) for n in re.findall(r"\d+", "10 apples, 25 pears and 7 figs")))
```

## 🔴 Challenge 3

```python
strong = re.compile(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}")
for pw in ["weak", "Password1", "alllowercase1"]:
    print(pw, bool(strong.fullmatch(pw)))
```

---
[⬅️ Back to the chapter](../../part-1-foundations/06-strings-and-regex.ipynb) | [🏠 Challenges bank](../README.md)
