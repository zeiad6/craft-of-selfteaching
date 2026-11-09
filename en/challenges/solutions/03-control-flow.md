# 🔑 Reference Solutions: Chapter 3: Control Flow & Conditional Logic

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## Shared imports

```python
import random
```

## 🟢 Challenge 1

```python
print([n for n in range(1, 21) if n % 2 == 0])
```

## 🟡 Challenge 2

```python
for n in range(1, 31):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
```

## 🔴 Challenge 3

```python
secret = random.randint(1, 100)
low, high, attempts = 1, 100, 0
while True:
    guess = (low + high) // 2
    attempts += 1
    if guess == secret:
        break
    if guess < secret:
        low = guess + 1
    else:
        high = guess - 1
print(f"{secret=} found in {attempts} attempts")
```

---
[⬅️ Back to the chapter](../../part-1-foundations/03-control-flow.ipynb) | [🏠 Challenges bank](../README.md)
