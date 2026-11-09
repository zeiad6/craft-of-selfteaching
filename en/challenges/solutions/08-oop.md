# 🔑 Reference Solutions: Chapter 8: Object-Oriented Programming (OOP)

> Try the challenges in the notebook first! Some solutions rely on earlier cells of the chapter (such as `Account` in Chapter 8 and `store` in Chapter 12), so run the chapter's cells first.

## Solutions

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
[⬅️ Back to the chapter](../../part-2-practice/08-oop.ipynb) | [🏠 Challenges bank](../README.md)
