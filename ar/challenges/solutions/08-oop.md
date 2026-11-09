<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل الثامن: البرمجة كائنية التوجه (Object-Oriented Programming - OOP)

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الحلول

```python
class Dog:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"{self.name} says woof"


print(Dog("Rex").speak())


class SafeAccount(Account):
    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount


s = SafeAccount("Sara", 10)
try:
    s.withdraw(50)
except ValueError as e:
    print("error:", e)


class Stack:
    def __init__(self) -> None:
        self._items: list = []

    def push(self, x) -> None:
        self._items.append(x)

    def pop(self):
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


st = Stack()
st.push(1)
st.push(2)
print(st.pop(), len(st), bool(st))
```

---
[⬅️ العودة إلى الفصل](../../part-2-practice/08-oop.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
