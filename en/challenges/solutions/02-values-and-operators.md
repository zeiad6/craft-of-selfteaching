# 🔑 Reference Solutions: Chapter 2: Values, Variables, and Operators

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## Shared imports

```python
# ✍️ Reference solutions (try on your own first!)
```

## 🟢 Challenge 1

```python
celsius: float = 37.0
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit:.2f}°F")
```

## 🟡 Challenge 2

```python
price = 250
discounted = price * (1 - 0.10)
final_total = discounted * (1 + 0.15)
print(f"Final total: {final_total:.2f}")
```

## 🔴 Challenge 3

```python
seconds = 100000
days, rest = divmod(seconds, 86400)
hours, rest = divmod(rest, 3600)
minutes, secs = divmod(rest, 60)
print(f"{days}d {hours}h {minutes}m {secs}s")
```

---
[⬅️ Back to the chapter](../../part-1-foundations/02-values-and-operators.ipynb) | [🏠 Challenges bank](../README.md)
