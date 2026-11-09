"""Builds chapters 5 and 6 notebooks (ar/en). Run: python scripts/build_chapters_5_6.py"""
import json
from build_chapters_3_4 import ROOT, nb, header, footer, md


def ch5(lang):
    ar = lang == "ar"
    c = [header(lang, "part-1-foundations/05-functions.ipynb",
                "🧱 الفصل الخامس: الدوال وتفكيك المشكلات (Functions)" if ar else "🧱 Chapter 5: Functions & Problem Decomposition",
                "قسِّم المشكلة الكبيرة إلى دوال صغيرة، تصبح كل واحدة منها سهلة الفهم والاختبار." if ar else
                "Break a big problem into small functions, each easy to understand and test.",
                ["تعريف الدوال باستخدام `def` وتمرير المعاملات وإرجاع القيم.",
                 "فهم المعاملات الافتراضية و`*args` و`**kwargs` والنطاق (Scope).",
                 "كتابة دوال مجهولة (`lambda`) ومُولِّدات (`yield`) ووثائق (Docstrings)."] if ar else
                ["Define functions with `def`, pass parameters and return values.",
                 "Understand default parameters, `*args`, `**kwargs`, and scope.",
                 "Write `lambda` functions, generators (`yield`), and docstrings."])]
    c.append(md(lang, "## 1. تعريف الدالة\n\nالدالة كتلة قابلة لإعادة الاستخدام. نكتب **تلميحات الأنواع** و**Docstring** لتوثيقها." if ar
                else "## 1. Defining a Function\n\nA function is a reusable block. We add **type hints** and a **docstring** to document it."))
    c.append(("code", '''
def area(width: float, height: float = 1.0) -> float:
    """Return the area of a rectangle."""
    return width * height


print(area(3, 4))
print(area(5))                    # default height
print(area(height=2, width=6))    # keyword arguments
help(area)
'''))
    c.append(md(lang, "## 2. معاملات مرنة والنطاق\n\n`*args` تجمع المعاملات الموضعية في صف، و`**kwargs` تجمع المسمّاة في قاموس. المتغير داخل الدالة محلي (Local) ولا يؤثر خارجها." if ar
                else "## 2. Flexible Parameters & Scope\n\n`*args` collects positional arguments into a tuple, `**kwargs` collects keyword ones into a dict. Variables inside a function are local."))
    c.append(("code", '''
def summarize(*numbers: int, **options: str) -> str:
    label = options.get("label", "total")
    return f"{label}: {sum(numbers)}"


print(summarize(1, 2, 3))
print(summarize(10, 20, label="sum"))

x = "global"


def shadow() -> None:
    x = "local"
    print(x)


shadow()
print(x)
'''))
    c.append(md(lang, "## 3. دوال `lambda` والمُولِّدات\n\nالمُولِّد (Generator) ينتج القيم عند الطلب بدل بناء قائمة كاملة في الذاكرة." if ar
                else "## 3. `lambda` and Generators\n\nA generator yields values on demand instead of building a full list in memory."))
    c.append(("code", '''
people = [("ali", 31), ("sara", 25), ("omar", 28)]
print(sorted(people, key=lambda p: p[1]))


def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


print(list(countdown(5)))
print(sum(i * i for i in range(1_000_000)))   # generator expression
'''))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** اكتب `is_even(n)` تُرجع `True` للأعداد الزوجية.
- 🟡 **متوسط:** اكتب `is_palindrome(text)` تتجاهل المسافات وحالة الأحرف.
- 🔴 **متقدم:** اكتب مُولِّد `fibonacci()` لا نهائياً، ثم خذ أول 10 قيم باستخدام `itertools.islice`.
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Write `is_even(n)` returning `True` for even numbers.
- 🟡 **Intermediate:** Write `is_palindrome(text)` ignoring spaces and letter case.
- 🔴 **Stretch:** Write an infinite `fibonacci()` generator, then take the first 10 values with `itertools.islice`.
"""))
    c.append(("code", '''
from itertools import islice


def is_even(n: int) -> bool:
    return n % 2 == 0


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    return cleaned == cleaned[::-1]


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(is_even(10), is_even(7))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Never odd or even"))
print(list(islice(fibonacci(), 10)))
'''))
    c.append(footer(lang, ("الفصل 4" if ar else "Chapter 4", "./04-data-structures.ipynb"),
                    ("الفصل 6: النصوص والتعابير النمطية" if ar else "Chapter 6 — Strings & Regex", "./06-strings-and-regex.ipynb")))
    return nb(c)


def ch6(lang):
    ar = lang == "ar"
    c = [header(lang, "part-1-foundations/06-strings-and-regex.ipynb",
                "🧱 الفصل السادس: النصوص والتعابير النمطية (Strings & Regex)" if ar else "🧱 Chapter 6: Strings & Regular Expressions",
                "معظم بيانات العالم الحقيقي نصوص، ومن يُتقن معالجتها يوفّر ساعات من العمل اليدوي." if ar else
                "Most real-world data is text, and mastering it saves hours of manual work.",
                ["التعامل مع النصوص: التقطيع والبحث والتنسيق.", "فهم أن النص `str` غير قابل للتعديل ودعم Unicode (العربية والإيموجي).",
                 "كتابة تعابير نمطية (Regular Expressions) بالوحدة `re`."] if ar else
                ["Slice, search, and format strings.", "Understand string immutability and Unicode (Arabic, emoji).",
                 "Write regular expressions with the `re` module."])]
    c.append(md(lang, "## 1. عمليات النصوص الأساسية\n\nالنص في بايثون يدعم Unicode كاملاً، فالعربية تعمل مباشرة. والنصوص **غير قابلة للتعديل**؛ كل دالة تُرجع نصاً جديداً." if ar
                else "## 1. Basic String Operations\n\nPython strings are fully Unicode, so Arabic works out of the box. Strings are **immutable**; every method returns a new string."))
    c.append(("code", '''
s = "  Self-Teaching is a Craft  "
print(s.strip().lower())
print(s.split())
print("-".join(["a", "b", "c"]))
print("Craft" in s, s.find("Craft"), s.strip()[:4], s.strip()[::-1])
print("مرحباً بالعالم".upper(), len("مرحباً"))
print(f"{3.14159:.2f} | {1234567:,} | {'x':>5} | {0.256:.1%}")
'''))
    c.append(md(lang, "## 2. التعابير النمطية (Regex)\n\nالتعبير النمطي لغة مصغّرة لوصف **أنماط النصوص**. استخدم نصوصاً خاماً `r\"...\"` كي لا تُفسَّر الشرطة المائلة.\n\n| الرمز | المعنى |\n| :-- | :-- |\n| `\\d` | رقم |\n| `\\w` | حرف أو رقم أو `_` |\n| `+` / `*` / `?` | مرة فأكثر / صفر فأكثر / اختياري |\n| `[...]` | أحد الأحرف |\n| `(...)` | مجموعة التقاط |" if ar
                else "## 2. Regular Expressions\n\nA regex is a mini-language for describing **text patterns**. Use raw strings `r\"...\"` so backslashes aren't interpreted.\n\n| Token | Meaning |\n| :-- | :-- |\n| `\\d` | digit |\n| `\\w` | letter, digit or `_` |\n| `+` / `*` / `?` | one+ / zero+ / optional |\n| `[...]` | any one of the characters |\n| `(...)` | capture group |"))
    c.append(("code", '''
import re

text = "Contact: ali@example.com, sara.k@mail.org | Tel: 2026-11-09"

emails = re.findall(r"[\\w.]+@[\\w.]+\\.\\w+", text)
print(emails)

m = re.search(r"(\\d{4})-(\\d{2})-(\\d{2})", text)
if m:
    year, month, day = m.groups()
    print(f"{year=} {month=} {day=}")

print(re.sub(r"\\d", "#", "Phone 0501234567"))
'''))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** عُدّ الحروف المتحركة الإنجليزية في جملة.
- 🟡 **متوسط:** استخرج كل الأرقام من نص واجمعها.
- 🔴 **متقدم:** تحقّق من قوة كلمة المرور بتعبير نمطي: 8 أحرف فأكثر، وتحتوي حرفاً كبيراً وصغيراً ورقماً.
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Count English vowels in a sentence.
- 🟡 **Intermediate:** Extract all numbers from a text and sum them.
- 🔴 **Stretch:** Validate password strength with regex: 8+ chars with an uppercase letter, a lowercase letter, and a digit.
"""))
    c.append(("code", '''
import re

# 1
print(sum(ch in "aeiou" for ch in "Self teaching is a craft".lower()))

# 2
print(sum(int(n) for n in re.findall(r"\\d+", "10 apples, 25 pears and 7 figs")))

# 3
strong = re.compile(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\\d).{8,}")
for pw in ["weak", "Password1", "alllowercase1"]:
    print(pw, bool(strong.fullmatch(pw)))
'''))
    c.append(footer(lang, ("الفصل 5" if ar else "Chapter 5", "./05-functions.ipynb"),
                    ("الفصل 7: الملفات" if ar else "Chapter 7 — File I/O", "../part-2-practice/07-file-io.ipynb")))
    return nb(c)


if __name__ == "__main__":
    for lang in ("ar", "en"):
        for name, fn in (("05-functions.ipynb", ch5), ("06-strings-and-regex.ipynb", ch6)):
            p = ROOT / lang / "part-1-foundations" / name
            p.write_text(json.dumps(fn(lang), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print("wrote", p)
