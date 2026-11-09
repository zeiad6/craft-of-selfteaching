<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل الثالث: التحكّم في التدفق والمنطق الشرطي (Control Flow)

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الاستيرادات المشتركة

```python
import random
```

## 🟢 التحدي 1

```python
print([n for n in range(1, 21) if n % 2 == 0])
```

## 🟡 التحدي 2

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

## 🔴 التحدي 3

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
[⬅️ العودة إلى الفصل](../../part-1-foundations/03-control-flow.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
