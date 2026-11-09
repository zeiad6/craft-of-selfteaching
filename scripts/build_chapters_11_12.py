"""Builds chapters 11-12 notebooks (ar/en). Run: python scripts/build_chapters_11_12.py"""
import json
from build_chapters_3_4 import ROOT, nb, header, footer, md

P = "part-3-mastery"


def ch11(lang):
    ar = lang == "ar"
    c = [header(lang, f"{P}/11-reading-docs.ipynb",
                "🚀 الفصل الحادي عشر: كيف تقرأ التوثيق الرسمي (Official Documentation)؟" if ar else "🚀 Chapter 11: How to Read Official Documentation",
                "من يستطيع قراءة التوثيق لا يحتاج إلى معلّم بعد اليوم." if ar else "Whoever can read the documentation never needs a teacher again.",
                ["استخدام `help()` و`dir()` و`inspect` للاستكشاف من داخل بايثون.", "قراءة توقيع الدالة (Signature) وفهم المعاملات.",
                 "التنقل في docs.python.org وإيجاد الإجابة بنفسك."] if ar else
                ["Explore from inside Python with `help()`, `dir()`, and `inspect`.", "Read a function signature and understand its parameters.",
                 "Navigate docs.python.org and find answers yourself."])]
    c.append(md(lang, """
## 1. المصدر الأول: بايثون نفسها

قبل البحث في الإنترنت اسأل المفسّر:

- `dir(obj)` ← ما الذي يمكنني فعله بهذا الكائن؟
- `help(obj)` ← كيف أستخدمه؟
- `type(obj)` ← ما نوعه؟
""" if ar else """
## 1. The First Source: Python Itself

Before searching the web, ask the interpreter:

- `dir(obj)` → what can I do with this object?
- `help(obj)` → how do I use it?
- `type(obj)` → what is it?
"""))
    c.append(("code", '''
import inspect

print([m for m in dir(str) if not m.startswith("_")][:12])
print(inspect.signature(str.split))
print(inspect.signature(sorted))
print(str.partition.__doc__)
'''))
    c.append(md(lang, """
## 2. تشريح توقيع الدالة

انظر إلى `sorted(iterable, /, *, key=None, reverse=False)`:

| الجزء | المعنى |
| :-- | :-- |
| `iterable` | معامل مطلوب |
| `/` | ما قبله **موضعي فقط** |
| `*` | ما بعده **بالاسم فقط** (Keyword-only) |
| `key=None` | معامل اختياري له قيمة افتراضية |

لذلك `sorted(data, reverse=True)` صحيحة، أما `sorted(data, True)` فتُسبب `TypeError`. هذه معلومة تعلّمتها من التوثيق لا من الحفظ.
""" if ar else """
## 2. Anatomy of a Signature

Look at `sorted(iterable, /, *, key=None, reverse=False)`:

| Part | Meaning |
| :-- | :-- |
| `iterable` | required parameter |
| `/` | everything before it is **positional-only** |
| `*` | everything after it is **keyword-only** |
| `key=None` | optional parameter with a default |

So `sorted(data, reverse=True)` is valid, while `sorted(data, True)` raises `TypeError`. You learned that from the docs, not from memorization.
"""))
    c.append(("code", '''
data = [3, 1, 2]
print(sorted(data, reverse=True))
try:
    sorted(data, True)
except TypeError as error:
    print("TypeError:", error)
'''))
    c.append(md(lang, """
## 3. التنقل في docs.python.org

1. **Tutorial**: للتعلّم المتسلسل.
2. **Library Reference**: لكل وحدة ودالة. هنا تقضي أغلب وقتك.
3. **Language Reference**: للقواعد الدقيقة للغة.
4. **What's New in Python 3.x**: لمعرفة المزايا الجديدة (مثل `itertools.batched` في 3.12).

**وصفة قراءة سريعة:** اقرأ أول فقرة، ثم الأمثلة، ثم المعاملات، وأخيراً ملاحظة `Changed in version` لتعرف إن كانت الميزة متوفرة عندك.
""" if ar else """
## 3. Navigating docs.python.org

1. **Tutorial**: sequential learning.
2. **Library Reference**: every module and function. You'll spend most of your time here.
3. **Language Reference**: precise language rules.
4. **What's New in Python 3.x**: discover new features (e.g. `itertools.batched` in 3.12).

**Quick-read recipe:** first paragraph, then the examples, then the parameters, and finally the `Changed in version` notes to check the feature exists in your version.
"""))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** باستخدام `help` فقط، اكتشف ما تفعله `str.zfill` ثم جرّبها.
- 🟡 **متوسط:** اقرأ توثيق `textwrap.shorten` واستخدمه لاختصار جملة إلى 20 حرفاً.
- 🔴 **متقدم:** اقرأ توثيق `itertools.pairwise` واستخدمه لحساب الفروق بين عناصر متتالية في قائمة.
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Using only `help`, discover what `str.zfill` does and try it.
- 🟡 **Intermediate:** Read the docs of `textwrap.shorten` and use it to trim a sentence to 20 characters.
- 🔴 **Stretch:** Read the docs of `itertools.pairwise` and use it to compute differences between consecutive items.
"""))
    c.append(("code", '''
import textwrap
from itertools import pairwise

print("42".zfill(5))
print(textwrap.shorten("Self-teaching is the craft behind every craft", width=20, placeholder="..."))
nums = [1, 4, 9, 16, 25]
print([b - a for a, b in pairwise(nums)])
'''))
    c.append(footer(lang, ("الفصل 10" if ar else "Chapter 10", "../part-2-practice/10-debugging-and-testing.ipynb"),
                    ("الفصل 12" if ar else "Chapter 12", "./12-beyond-basics.ipynb")))
    return nb(c)


def ch12(lang):
    ar = lang == "ar"
    c = [header(lang, f"{P}/12-beyond-basics.ipynb",
                "🚀 الفصل الثاني عشر: بناء المشاريع الحقيقية وما بعد الأساسيات" if ar else "🚀 Chapter 12: Building Real Projects & Moving Beyond the Basics",
                "تتعلّم أكثر من مشروع واحد تُنهيه مما تتعلّمه من عشر دورات تشاهدها." if ar else "You learn more from one project you finish than from ten courses you watch.",
                ["بناء أداة سطر أوامر كاملة (To-Do) تجمع ما تعلّمناه.", "استخدام `argparse` و`json` و`pathlib` و`dataclass` معاً.",
                 "رسم خطة تعلّم مستمرة بعد الكتاب."] if ar else
                ["Build a complete command-line To-Do tool combining everything so far.", "Use `argparse`, `json`, `pathlib`, and `dataclass` together.",
                 "Draw up a continuing learning plan beyond this book."])]
    c.append(md(lang, """
## 1. المشروع: مدير مهام بسطر الأوامر

**منهجية بناء أي مشروع:** (1) حدّد أصغر نسخة مفيدة، (2) فكّكها لدوال، (3) اختبر كل جزء، (4) وسّع تدريجياً.

سنخزّن المهام في ملف JSON ونتحكم بها عبر أوامر `add` و`list` و`done`.
""" if ar else """
## 1. The Project: A Command-Line Task Manager

**How to build any project:** (1) define the smallest useful version, (2) decompose into functions, (3) test each piece, (4) expand gradually.

We'll store tasks in a JSON file and control them with `add`, `list`, and `done` commands.
"""))
    c.append(("code", '''
import argparse
import json
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


def load(path: Path) -> list[Task]:
    if not path.exists():
        return []
    return [Task(**item) for item in json.loads(path.read_text(encoding="utf-8"))]


def save(path: Path, tasks: list[Task]) -> None:
    path.write_text(json.dumps([asdict(t) for t in tasks], ensure_ascii=False, indent=2), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    add = sub.add_parser("add")
    add.add_argument("title")
    done = sub.add_parser("done")
    done.add_argument("id", type=int)
    return parser


def run(argv: list[str], path: Path) -> None:
    args = build_parser().parse_args(argv)
    tasks = load(path)
    match args.command:
        case "add":
            tasks.append(Task(id=len(tasks) + 1, title=args.title))
            save(path, tasks)
            print(f"added #{len(tasks)}: {args.title}")
        case "done":
            for t in tasks:
                if t.id == args.id:
                    t.done = True
            save(path, tasks)
            print(f"completed #{args.id}")
        case "list":
            for t in tasks:
                print(f"[{'x' if t.done else ' '}] {t.id}. {t.title}")


store = Path(tempfile.mkdtemp()) / "tasks.json"
run(["add", "Read chapter 12"], store)
run(["add", "اكتب مشروعك الأول"], store)
run(["done", "1"], store)
run(["list"], store)
'''))
    c.append(md(lang, """
## 2. خطتك بعد الكتاب

| المسار | الخطوة التالية | مورد للتعلّم الذاتي |
| :-- | :-- | :-- |
| الويب | Flask أو FastAPI | التوثيق الرسمي لكل إطار |
| البيانات | pandas وmatplotlib | دفاتر Jupyter وبيانات Kaggle |
| الأتمتة | `requests` و`selenium` | أتمتة مهام عملك اليومي |
| الذكاء الاصطناعي | scikit-learn ثم PyTorch | الكتب المفتوحة وأوراق البحث |

**قاعدة ذهبية:** اختر مشكلة حقيقية تواجهك، وابنِ لها حلاً صغيراً، وانشره على GitHub.
""" if ar else """
## 2. Your Plan After This Book

| Track | Next step | Self-teaching resource |
| :-- | :-- | :-- |
| Web | Flask or FastAPI | each framework's official docs |
| Data | pandas and matplotlib | Jupyter notebooks and Kaggle datasets |
| Automation | `requests` and `selenium` | automate your own daily tasks |
| AI | scikit-learn, then PyTorch | open books and research papers |

**Golden rule:** pick a real problem you face, build a small solution, and publish it on GitHub.
"""))
    c.append(md(lang, """
---

## 💻 تحديات برمجية تطبيقية

- 🟢 **مبتدئ:** أضف أمر `clear` يحذف المهام المنجزة.
- 🟡 **متوسط:** أضف أمر `remove ID` وتحقق من أن المعرّف موجود قبل الحذف.
- 🔴 **متقدم:** أضف أولوية `--priority {low,medium,high}` وفرز القائمة بحسبها.

وهذا هو تحدّيك الأخير: **أنهِ مشروعاً من اختيارك وانشره.**
""" if ar else """
---

## 💻 Coding Challenges

- 🟢 **Warm-up:** Add a `clear` command that deletes completed tasks.
- 🟡 **Intermediate:** Add `remove ID`, verifying the ID exists before deleting.
- 🔴 **Stretch:** Add `--priority {low,medium,high}` and sort the list by it.

And your final challenge: **finish a project of your own choosing and publish it.**
"""))
    c.append(("code", '''
# 1: reference solution for `clear` (extend run() the same way)
def clear_done(path: Path) -> int:
    tasks = load(path)
    remaining = [t for t in tasks if not t.done]
    save(path, remaining)
    return len(tasks) - len(remaining)


print("removed:", clear_done(store))
run(["list"], store)
'''))
    c.append(footer(lang, ("الفصل 11" if ar else "Chapter 11", "./11-reading-docs.ipynb"),
                    ("الملحق أ: بيئة العمل" if ar else "Appendix A — Setup", "../appendices/01-setup-environment.md")))
    return nb(c)


if __name__ == "__main__":
    for lang in ("ar", "en"):
        for name, fn in (("11-reading-docs.ipynb", ch11), ("12-beyond-basics.ipynb", ch12)):
            p = ROOT / lang / P / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(fn(lang), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print("wrote", p)
