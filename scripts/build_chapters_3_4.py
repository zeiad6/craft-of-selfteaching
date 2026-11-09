"""Builds chapters 3 and 4 notebooks (ar/en). Run: python scripts/build_chapters_3_4.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "zeiad6/craft-of-selfteaching"


def nb(cells):
    out = []
    for i, (kind, text) in enumerate(cells):
        cell = {"cell_type": kind, "id": f"c{i:02d}", "metadata": {},
                "source": text.strip("\n").splitlines(keepends=True)}
        if kind == "code":
            cell.update(execution_count=None, outputs=[])
        out.append(cell)
    return {"cells": out,
            "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                         "language_info": {"name": "python", "version": "3.12.0"}},
            "nbformat": 4, "nbformat_minor": 5}


def rtl(t):
    return f'<div dir="rtl">\n\n{t.strip()}\n\n</div>'


def header(lang, path, title, quote, goals):
    badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/{REPO}/blob/main/{lang}/{path})"
    g = "\n".join(f"{i}. {x}" for i, x in enumerate(goals, 1))
    head = "🎯 أهداف هذا الفصل" if lang == "ar" else "🎯 Learning Objectives"
    body = f"{badge}\n\n# {title}\n\n> **{quote}**\n\n---\n\n## {head}\n{g}"
    return ("markdown", rtl(body) if lang == "ar" else body)


def footer(lang, prev_, nxt):
    if lang == "ar":
        t = f'<div dir="rtl" align="center">\n\n---\n\n[**➡️ السابق: {prev_[0]}**]({prev_[1]}) | [**🏠 الفهرس العربي**](../README.md) | [**التالي: {nxt[0]} ⬅️**]({nxt[1]})\n\n</div>'
    else:
        t = f'---\n\n<div align="center">\n\n[**⬅️ Previous: {prev_[0]}**]({prev_[1]}) | [**🏠 English Index**](../README.md) | [**Next: {nxt[0]} ➡️**]({nxt[1]})\n\n</div>'
    return ("markdown", t)


def md(lang, t):
    return ("markdown", rtl(t) if lang == "ar" else t)


# ---------------------------------------------------------------- Chapter 3
def ch3(lang):
    ar = lang == "ar"
    c = [header(lang, "part-1-foundations/03-control-flow.ipynb",
                "🧱 الفصل الثالث: التحكّم في التدفق والمنطق الشرطي (Control Flow)" if ar else "🧱 Chapter 3: Control Flow & Conditional Logic",
                "البرنامج الذي لا يتخذ قرارات ليس إلا آلة حاسبة." if ar else "A program that makes no decisions is just a calculator.",
                ["كتابة قرارات بـ `if / elif / else`.", "التكرار بـ `for` و`while` مع `break` و`continue`.",
                 "استخدام **مطابقة الأنماط الهيكلية (`match / case`)** الحديثة."] if ar else
                ["Make decisions with `if / elif / else`.", "Repeat work with `for` and `while`, plus `break` and `continue`.",
                 "Use modern **structural pattern matching (`match / case`)**."])]
    c.append(md(lang, """
## 1. الجمل الشرطية (Conditional Statements)

بايثون تحدّد الكتل **بالإزاحة (Indentation)** — أربع مسافات — لا بالأقواس. القراءة الدقيقة هنا حاسمة!
""" if ar else """
## 1. Conditional Statements

Python marks blocks by **indentation**—four spaces—not braces. Careful reading matters here!
"""))
    c.append(("code", """
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(f"{score=} -> {grade=}")
"""))
    c.append(md(lang, """
## 2. حلقات التكرار (Loops)

- `for` للمرور على كائن قابل للتكرار (Iterable) مثل `range()` أو نص أو قائمة.
- `while` للتكرار ما دام الشرط صحيحاً — احذر الحلقات اللانهائية!
""" if ar else """
## 2. Loops

- `for` walks over an iterable such as `range()`, a string, or a list.
- `while` repeats as long as a condition holds—beware infinite loops!
"""))
    c.append(("code", """
for i in range(1, 6):
    if i == 2:
        continue          # skip 2
    if i == 5:
        break             # stop before 5
    print(i)

n = 27
steps = 0
while n != 1:             # Collatz sequence
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps += 1
print(f"{steps=}")
"""))
    c.append(md(lang, """
## 3. مطابقة الأنماط الهيكلية (`match / case`) — Python 3.10+

بديل أوضح من سلسلة `elif` طويلة، ويستطيع تفكيك البيانات أيضاً.
""" if ar else """
## 3. Structural Pattern Matching (`match / case`) — Python 3.10+

A clearer alternative to long `elif` chains that can also destructure data.
"""))
    c.append(("code", """
def describe(command: str | tuple) -> str:
    match command:
        case "start" | "run":
            return "starting"
        case ("move", x, y):
            return f"moving to ({x}, {y})"
        case ("say", *words):
            return " ".join(words)
        case _:
            return "unknown command"


print(describe("run"))
print(describe(("move", 3, 4)))
print(describe(("say", "hello", "world")))
print(describe(42))
"""))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** اطبع الأعداد الزوجية من 1 إلى 20.
- 🟡 **متوسط:** FizzBuzz: اطبع 1–30، و`Fizz` لمضاعفات 3، و`Buzz` لمضاعفات 5، و`FizzBuzz` لمضاعفات الاثنين.
- 🔴 **متقدم:** لعبة تخمين: يختار البرنامج رقماً سرياً بين 1 و100 باستخدام `random.randint`، ويحاول البرنامج إيجاده بالبحث الثنائي ويطبع عدد المحاولات.
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Print the even numbers from 1 to 20.
- 🟡 **Intermediate:** FizzBuzz: print 1–30; `Fizz` for multiples of 3, `Buzz` for 5, `FizzBuzz` for both.
- 🔴 **Stretch:** Guessing game: pick a secret number in 1–100 with `random.randint`, then find it by binary search and print the number of attempts.
"""))
    c.append(("code", """
import random

# 1
print([n for n in range(1, 21) if n % 2 == 0])

# 2
for n in range(1, 31):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# 3
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
"""))
    c.append(footer(lang, ("الفصل 2" if ar else "Chapter 2", "./02-values-and-operators.ipynb"),
                    ("الفصل 4: هياكل البيانات" if ar else "Chapter 4 — Data Structures", "./04-data-structures.ipynb")))
    return nb(c)


# ---------------------------------------------------------------- Chapter 4
def ch4(lang):
    ar = lang == "ar"
    c = [header(lang, "part-1-foundations/04-data-structures.ipynb",
                "🧱 الفصل الرابع: هياكل البيانات الأساسية (Data Structures)" if ar else "🧱 Chapter 4: Core Data Structures",
                "اختر الهيكل المناسب للبيانات يصبح نصف المشكلة محلولاً." if ar else "Choose the right structure for your data and half the problem is solved.",
                ["التعامل مع القوائم `list` والصفوف `tuple`.", "استخدام القواميس `dict` والمجموعات `set`.",
                 "كتابة **القوائم المختصرة (List Comprehensions)** وفهم القابل وغير القابل للتعديل."] if ar else
                ["Work with `list` and `tuple`.", "Use `dict` and `set`.",
                 "Write **list comprehensions** and understand mutable vs. immutable."])]
    c.append(md(lang, "## 1. القوائم والصفوف (Lists & Tuples)\n\nالقائمة `[]` قابلة للتعديل، والصف `()` غير قابل للتعديل." if ar
                else "## 1. Lists & Tuples\n\nA list `[]` is mutable; a tuple `()` is immutable."))
    c.append(("code", """
langs = ["python", "go", "rust"]
langs.append("c")
langs[0] = "Python"
print(langs, langs[-1], langs[1:3], len(langs))

point = (3, 4)
x, y = point               # unpacking
print(x, y)

try:
    point[0] = 9
except TypeError as error:
    print(f"tuples are immutable: {error}")
"""))
    c.append(md(lang, "## 2. القواميس والمجموعات (Dicts & Sets)\n\nالقاموس يربط مفتاحاً بقيمة، والمجموعة تحتفظ بالعناصر الفريدة فقط." if ar
                else "## 2. Dicts & Sets\n\nA dict maps keys to values; a set keeps unique elements only."))
    c.append(("code", """
person = {"name": "Ziad", "age": 30}
person["city"] = "Riyadh"
print(person.get("email", "n/a"))
for key, value in person.items():
    print(key, "->", value)

a, b = {1, 2, 3}, {3, 4}
print(a | b, a & b, a - b)
print(set([1, 1, 2, 2, 3]))
"""))
    c.append(md(lang, "## 3. القوائم المختصرة (Comprehensions)\n\nصياغة أنيقة لبناء قائمة أو قاموس في سطر واحد." if ar
                else "## 3. Comprehensions\n\nA concise way to build lists and dicts in one line."))
    c.append(("code", """
squares = [n * n for n in range(1, 8) if n % 2]
lengths = {w: len(w) for w in ["apple", "fig", "banana"]}
print(squares)
print(lengths)

# Modern typing: built-in generics
scores: dict[str, list[int]] = {"ali": [90, 85], "sara": [78]}
print({k: sum(v) / len(v) for k, v in scores.items()})
"""))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** أزل التكرار من `[3, 1, 3, 2, 1]` مع الحفاظ على الترتيب.
- 🟡 **متوسط:** عُدّ تكرار كل كلمة في جملة وأظهر أكثر كلمة تكراراً.
- 🔴 **متقدم:** اعكس قاموساً `{مفتاح: قيمة}` إلى `{قيمة: [مفاتيح]}` مع التعامل مع القيم المكررة.
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Remove duplicates from `[3, 1, 3, 2, 1]` while preserving order.
- 🟡 **Intermediate:** Count word frequencies in a sentence and show the most common word.
- 🔴 **Stretch:** Invert a dict `{key: value}` into `{value: [keys]}`, handling duplicate values.
"""))
    c.append(("code", """
from collections import Counter, defaultdict

# 1
print(list(dict.fromkeys([3, 1, 3, 2, 1])))

# 2
sentence = "the quick brown fox jumps over the lazy dog the end"
counts = Counter(sentence.split())
print(counts.most_common(1))

# 3
original = {"a": 1, "b": 2, "c": 1}
inverted = defaultdict(list)
for key, value in original.items():
    inverted[value].append(key)
print(dict(inverted))
"""))
    c.append(footer(lang, ("الفصل 3" if ar else "Chapter 3", "./03-control-flow.ipynb"),
                    ("الفصل 5: الدوال" if ar else "Chapter 5 — Functions", "./05-functions.ipynb")))
    return nb(c)


if __name__ == "__main__":
    for lang in ("ar", "en"):
        for name, fn in (("03-control-flow.ipynb", ch3), ("04-data-structures.ipynb", ch4)):
            p = ROOT / lang / "part-1-foundations" / name
            p.write_text(json.dumps(fn(lang), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print("wrote", p)
