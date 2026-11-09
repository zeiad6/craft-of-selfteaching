"""Builds chapters 7-10 notebooks (ar/en). Run: python scripts/build_chapters_7_10.py"""
import json
from build_chapters_3_4 import ROOT, nb, header, footer, md

P = "part-2-practice"


def ch7(lang):
    ar = lang == "ar"
    c = [header(lang, f"{P}/07-file-io.ipynb",
                "🛠️ الفصل السابع: التعامل مع الملفات (File I/O)" if ar else "🛠️ Chapter 7: File I/O & Data Persistence",
                "البرنامج الذي ينسى كل شيء عند إغلاقه محدود الفائدة؛ الملفات تمنحه ذاكرة." if ar else
                "A program that forgets everything when it closes is of limited use; files give it memory.",
                ["قراءة وكتابة الملفات النصية بأمان باستخدام `with`.", "التعامل مع المسارات عبر `pathlib` الحديثة.",
                 "حفظ البيانات بصيغتي JSON وCSV."] if ar else
                ["Read and write text files safely with `with`.", "Handle paths using modern `pathlib`.",
                 "Persist data as JSON and CSV."])]
    c.append(md(lang, "## 1. القراءة والكتابة\n\nعبارة `with` تُغلق الملف تلقائياً حتى لو حدث خطأ. حدّد الترميز `encoding=\"utf-8\"` دائماً، خاصةً مع العربية على Windows. نستخدم هنا مجلداً مؤقتاً كي لا نترك ملفات على جهازك." if ar
                else "## 1. Reading & Writing\n\n`with` closes the file automatically even if an error occurs. Always pass `encoding=\"utf-8\"`, especially for Arabic on Windows. We use a temporary folder so nothing is left on your machine."))
    c.append(("code", '''
import tempfile
from pathlib import Path

workdir = Path(tempfile.mkdtemp())
note = workdir / "note.txt"

note.write_text("سطر أول\\nline two\\n", encoding="utf-8")

with note.open("a", encoding="utf-8") as f:
    f.write("third line\\n")

for number, line in enumerate(note.read_text(encoding="utf-8").splitlines(), 1):
    print(number, line)

print(note.name, note.suffix, note.stem, note.exists(), note.stat().st_size)
'''))
    c.append(md(lang, "## 2. JSON وCSV" if ar else "## 2. JSON & CSV"))
    c.append(("code", '''
import csv
import json

data = {"name": "Ziad", "skills": ["python", "git"], "level": 3}
js = workdir / "profile.json"
js.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.loads(js.read_text(encoding="utf-8"))["skills"])

rows = [{"name": "ali", "score": 90}, {"name": "sara", "score": 85}]
cs = workdir / "scores.csv"
with cs.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)

with cs.open(newline="", encoding="utf-8") as f:
    print([r for r in csv.DictReader(f)])

for p in sorted(workdir.glob("*")):
    print(p.name)
'''))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** اكتب 5 أسطر في ملف ثم اقرأه واطبع عدد الأسطر.
- 🟡 **متوسط:** اقرأ ملفاً نصياً وأنشئ ملف JSON فيه تكرار كل كلمة.
- 🔴 **متقدم:** اكتب دالة `find_files(root, suffix)` تبحث بشكل تكراري عن الملفات بامتداد معيّن بـ `rglob`.
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Write 5 lines to a file, read it back, and print the line count.
- 🟡 **Intermediate:** Read a text file and write a JSON file with each word's frequency.
- 🔴 **Stretch:** Write `find_files(root, suffix)` that recursively finds files with a given extension using `rglob`.
"""))
    c.append(("code", '''
from collections import Counter

# 1
f1 = workdir / "five.txt"
f1.write_text("\\n".join(f"line {i}" for i in range(1, 6)), encoding="utf-8")
print(len(f1.read_text(encoding="utf-8").splitlines()))

# 2
words = "to be or not to be".split()
freq = workdir / "freq.json"
freq.write_text(json.dumps(Counter(words)), encoding="utf-8")
print(freq.read_text(encoding="utf-8"))


# 3
def find_files(root: Path, suffix: str) -> list[Path]:
    return sorted(root.rglob(f"*{suffix}"))


print([p.name for p in find_files(workdir, ".json")])
'''))
    c.append(footer(lang, ("الفصل 6" if ar else "Chapter 6", "../part-1-foundations/06-strings-and-regex.ipynb"),
                    ("الفصل 8: البرمجة كائنية التوجه" if ar else "Chapter 8 — OOP", "./08-oop.ipynb")))
    return nb(c)


def ch8(lang):
    ar = lang == "ar"
    c = [header(lang, f"{P}/08-oop.ipynb",
                "🛠️ الفصل الثامن: البرمجة كائنية التوجه (Object-Oriented Programming - OOP)" if ar else "🛠️ Chapter 8: Object-Oriented Programming (OOP)",
                "الفئة قالب، والكائن شيء حقيقي مصنوع من ذلك القالب." if ar else "A class is a blueprint; an object is a real thing built from it.",
                ["تعريف الفئات (Classes) والكائنات والسمات والدوال التابعة (Methods).", "فهم الوراثة (Inheritance) وتعدّد الأشكال (Polymorphism).",
                 "استخدام `@dataclass` الحديثة لتقليل الكود المكرر."] if ar else
                ["Define classes, objects, attributes, and methods.", "Understand inheritance and polymorphism.",
                 "Use the modern `@dataclass` to cut boilerplate."])]
    c.append(md(lang, "## 1. الفئة والكائن\n\n`__init__` هي الدالة التي تُنفَّذ عند إنشاء الكائن، و`self` يشير إلى الكائن نفسه." if ar
                else "## 1. Class & Object\n\n`__init__` runs when an object is created, and `self` refers to the object itself."))
    c.append(("code", '''
class Account:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance          # leading underscore: "internal"

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def __repr__(self) -> str:
        return f"Account({self.owner!r}, {self._balance})"


acc = Account("Ziad", 100)
acc.deposit(50)
print(acc, acc.balance)
'''))
    c.append(md(lang, "## 2. الوراثة وتعدّد الأشكال" if ar else "## 2. Inheritance & Polymorphism"))
    c.append(("code", '''
class Shape:
    def area(self) -> float:
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2


class Circle(Shape):
    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        return 3.14159 * self.r ** 2


for shape in (Square(2), Circle(1)):       # same call, different behavior
    print(type(shape).__name__, round(shape.area(), 2))
'''))
    c.append(md(lang, "## 3. فئات البيانات `@dataclass`\n\nتولّد `__init__` و`__repr__` و`__eq__` تلقائياً." if ar
                else "## 3. `@dataclass`\n\nGenerates `__init__`, `__repr__`, and `__eq__` automatically."))
    c.append(("code", '''
from dataclasses import dataclass, field


@dataclass(order=True)
class Book:
    title: str
    pages: int
    tags: list[str] = field(default_factory=list)


a, b = Book("A", 200), Book("B", 150, ["python"])
print(a, a == Book("A", 200), a > b)
'''))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** عرّف فئة `Dog` لها `name` ودالة `speak()`.
- 🟡 **متوسط:** في `Account` أضف `withdraw` التي ترفع خطأً عند عدم كفاية الرصيد.
- 🔴 **متقدم:** صمّم `Stack` بدالتي `push` و`pop` مع `__len__` و`__bool__`.
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Define a `Dog` class with `name` and a `speak()` method.
- 🟡 **Intermediate:** Add `withdraw` to `Account` that raises an error on insufficient funds.
- 🔴 **Stretch:** Design a `Stack` with `push` and `pop`, plus `__len__` and `__bool__`.
"""))
    c.append(("code", '''
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
'''))
    c.append(footer(lang, ("الفصل 7" if ar else "Chapter 7", "./07-file-io.ipynb"),
                    ("الفصل 9: الوحدات" if ar else "Chapter 9 — Modules", "./09-modules.ipynb")))
    return nb(c)


def ch9(lang):
    ar = lang == "ar"
    c = [header(lang, f"{P}/09-modules.ipynb",
                "🛠️ الفصل التاسع: الوحدات والمكتبات (Modules & Packages)" if ar else "🛠️ Chapter 9: Modules, Packages & The Python Ecosystem",
                "لا تعِد اختراع العجلة؛ تعلّم كيف تجد الأدوات الجاهزة وتستخدمها." if ar else "Don't reinvent the wheel; learn to find ready-made tools and use them.",
                ["استيراد الوحدات من المكتبة القياسية.", "إنشاء وحدتك الخاصة وفهم `if __name__ == \"__main__\"`.",
                 "إنشاء بيئة افتراضية وتثبيت حزم عبر `pip` أو `uv`."] if ar else
                ["Import modules from the standard library.", "Create your own module and understand `if __name__ == \"__main__\"`.",
                 "Create a virtual environment and install packages with `pip` or `uv`."])]
    c.append(md(lang, "## 1. الاستيراد\n\nبايثون تأتي مع «بطاريات مضمّنة»: مئات الوحدات الجاهزة. استكشفها بـ `dir()` و`help()`." if ar
                else "## 1. Importing\n\nPython ships \"batteries included\": hundreds of ready modules. Explore them with `dir()` and `help()`."))
    c.append(("code", '''
import math
import statistics
from datetime import date, timedelta
from random import choice

print(math.sqrt(144), math.pi)
print(statistics.mean([2, 4, 9]), statistics.median([2, 4, 9]))
print(date(2026, 11, 9) + timedelta(days=30))
print(choice(["a", "b", "c"]) in "abc")
print([n for n in dir(math) if n.startswith("fa")])
'''))
    c.append(md(lang, "## 2. وحدتك الخاصة\n\nأي ملف `.py` هو وحدة. الشرط `__name__ == \"__main__\"` يتحقق فقط عند تشغيل الملف مباشرة لا عند استيراده. سننشئ وحدة مؤقتة ونستوردها." if ar
                else "## 2. Your Own Module\n\nAny `.py` file is a module. The `__name__ == \"__main__\"` guard runs only when the file is executed directly, not when imported. We'll create a temporary module and import it."))
    c.append(("code", '''
import importlib
import sys
import tempfile
from pathlib import Path

tmp = Path(tempfile.mkdtemp())
(tmp / "greeter.py").write_text(
    "def hello(name: str) -> str:\\n"
    "    return f'Hello, {name}!'\\n\\n"
    "if __name__ == '__main__':\\n"
    "    print('run directly')\\n",
    encoding="utf-8",
)
sys.path.insert(0, str(tmp))
greeter = importlib.import_module("greeter")
print(greeter.hello("Ziad"), greeter.__name__)
'''))
    c.append(md(lang, """
## 3. البيئات الافتراضية والحزم الخارجية

```bash
# الطريقة الكلاسيكية
python -m venv .venv
pip install requests

# الطريقة الحديثة والأسرع (uv)
uv venv
uv pip install requests
```

سجّل المتطلبات في `requirements.txt` أو `pyproject.toml` لتتمكن من إعادة بناء البيئة.
""" if ar else """
## 3. Virtual Environments & Third-Party Packages

```bash
# Classic way
python -m venv .venv
pip install requests

# Modern, faster way (uv)
uv venv
uv pip install requests
```

Record dependencies in `requirements.txt` or `pyproject.toml` so the environment can be rebuilt.
"""))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** احسب عدد الأيام بين اليوم و1 يناير 2027 بـ `datetime`.
- 🟡 **متوسط:** استخدم `collections.Counter` و`statistics` لحساب المنوال لقائمة أرقام.
- 🔴 **متقدم:** أنشئ حزمة صغيرة بمجلد و`__init__.py` تحتوي وحدتين واستوردها.
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Compute the days from today until 1 Jan 2027 using `datetime`.
- 🟡 **Intermediate:** Use `collections.Counter` and `statistics` to find the mode of a list.
- 🔴 **Stretch:** Create a small package (folder + `__init__.py`) with two modules and import it.
"""))
    c.append(("code", '''
from collections import Counter
from datetime import date
import statistics

# 1
print((date(2027, 1, 1) - date.today()).days >= 0)

# 2
nums = [1, 2, 2, 3, 3, 3, 4]
print(Counter(nums).most_common(1)[0][0], statistics.mode(nums))

# 3
pkg = tmp / "mytools"
pkg.mkdir(exist_ok=True)
(pkg / "__init__.py").write_text("from .maths import double\\n", encoding="utf-8")
(pkg / "maths.py").write_text("def double(x):\\n    return x * 2\\n", encoding="utf-8")
mytools = importlib.import_module("mytools")
print(mytools.double(21))
'''))
    c.append(footer(lang, ("الفصل 8" if ar else "Chapter 8", "./08-oop.ipynb"),
                    ("الفصل 10: الاختبارات" if ar else "Chapter 10 — Debugging & Testing", "./10-debugging-and-testing.ipynb")))
    return nb(c)


def ch10(lang):
    ar = lang == "ar"
    c = [header(lang, f"{P}/10-debugging-and-testing.ipynb",
                "🛠️ الفصل العاشر: الاختبارات ومعالجة الأخطاء (Debugging & Testing)" if ar else "🛠️ Chapter 10: Debugging, Exceptions & Testing",
                "المبرمج المحترف لا يتجنب الأخطاء، بل يصطادها مبكراً بالاختبارات." if ar else "A professional doesn't avoid bugs; they catch them early with tests.",
                ["معالجة الاستثناءات بـ `try / except / else / finally`.", "التنقيح بالطباعة و`breakpoint()` و`logging`.",
                 "كتابة اختبارات وحدات (Unit Tests) بـ `unittest` والتعرّف على `pytest`."] if ar else
                ["Handle exceptions with `try / except / else / finally`.", "Debug with prints, `breakpoint()`, and `logging`.",
                 "Write unit tests with `unittest` and meet `pytest`."])]
    c.append(md(lang, "## 1. الاستثناءات (Exceptions)\n\nاصطد الأخطاء **المحددة** التي تتوقعها، ولا تستخدم `except:` المجردة التي تُخفي الأخطاء الحقيقية." if ar
                else "## 1. Exceptions\n\nCatch the **specific** errors you expect; avoid bare `except:` which hides real bugs."))
    c.append(("code", '''
def parse_age(text: str) -> int:
    try:
        age = int(text)
    except ValueError:
        raise ValueError(f"not a number: {text!r}") from None
    else:
        if age < 0:
            raise ValueError("age cannot be negative")
        return age
    finally:
        print("checked", repr(text))


for sample in ["30", "abc", "-5"]:
    try:
        print("age =", parse_age(sample))
    except ValueError as error:
        print("error:", error)
'''))
    c.append(md(lang, "## 2. التنقيح (Debugging)\n\nاستخدم `logging` بدل `print` في المشاريع الجادة؛ فهو يدعم المستويات ويمكن إيقافه. وللتوقف التفاعلي اكتب `breakpoint()` داخل الكود." if ar
                else "## 2. Debugging\n\nPrefer `logging` over `print` in serious projects; it supports levels and can be switched off. For interactive stepping, put `breakpoint()` in your code."))
    c.append(("code", '''
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s", force=True)
log = logging.getLogger("demo")


def average(values: list[float]) -> float:
    log.debug("values=%s", values)
    if not values:
        log.warning("empty list, returning 0")
        return 0.0
    return sum(values) / len(values)


print(average([1, 2, 3]))
print(average([]))
'''))
    c.append(md(lang, "## 3. اختبارات الوحدات\n\nاكتب اختباراً يصف السلوك المتوقع **قبل** إصلاح الخطأ. `unittest` مضمّنة، و`pytest` أبسط صياغة (`pip install pytest`) وتكفي فيها دوال عادية و`assert`." if ar
                else "## 3. Unit Tests\n\nWrite a test describing the expected behavior **before** fixing a bug. `unittest` is built in; `pytest` has simpler syntax (`pip install pytest`)—plain functions and `assert` are enough."))
    c.append(("code", '''
import unittest


def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


class TestLeap(unittest.TestCase):
    def test_common(self):
        self.assertTrue(is_leap(2024))
        self.assertFalse(is_leap(2023))

    def test_century_rules(self):
        self.assertFalse(is_leap(1900))
        self.assertTrue(is_leap(2000))


suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestLeap)
result = unittest.TextTestRunner(verbosity=2).run(suite)
print("all passed:", result.wasSuccessful())
'''))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** اكتب دالة قسمة آمنة تُرجع `None` عند القسمة على صفر.
- 🟡 **متوسط:** اكتب اختبارات لدالة `is_palindrome` من الفصل الخامس.
- 🔴 **متقدم:** اكتب مُزخرِفاً (Decorator) `@retry(times=3)` يعيد المحاولة عند ظهور استثناء.
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Write a safe division function that returns `None` on division by zero.
- 🟡 **Intermediate:** Write tests for the `is_palindrome` function from Chapter 5.
- 🔴 **Stretch:** Write a `@retry(times=3)` decorator that retries when an exception occurs.
"""))
    c.append(("code", '''
import functools


# 1
def safe_div(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None


print(safe_div(6, 3), safe_div(1, 0))


# 2
def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    return cleaned == cleaned[::-1]


class TestPalindrome(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(is_palindrome("Never odd or even"))
        self.assertFalse(is_palindrome("python"))


print(unittest.TextTestRunner().run(
    unittest.defaultTestLoader.loadTestsFromTestCase(TestPalindrome)).wasSuccessful())


# 3
def retry(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    print(f"attempt {attempt} failed: {exc}")
                    if attempt == times:
                        raise
        return wrapper
    return decorator


calls = {"n": 0}


@retry(times=3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise RuntimeError("temporary failure")
    return "success"


print(flaky())
'''))
    c.append(footer(lang, ("الفصل 9" if ar else "Chapter 9", "./09-modules.ipynb"),
                    ("الفصل 11: قراءة التوثيق" if ar else "Chapter 11 — Reading Docs", "../part-3-mastery/11-reading-docs.ipynb")))
    return nb(c)


if __name__ == "__main__":
    items = (("07-file-io.ipynb", ch7), ("08-oop.ipynb", ch8), ("09-modules.ipynb", ch9),
             ("10-debugging-and-testing.ipynb", ch10))
    for lang in ("ar", "en"):
        for name, fn in items:
            p = ROOT / lang / P / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(fn(lang), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print("wrote", p)
