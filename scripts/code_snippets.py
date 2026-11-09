"""Authentic Python 3.12+ code snippets for all 13 video chapters and scenes.

Code remains strictly in its original English/code format for both
Arabic and English video rendering pipelines.
"""

CHAPTER_SNIPPETS: dict[str, list[str]] = {
    "00-preface": [
        (
            "# 01. The Core Philosophy of Self-Teaching\n"
            "def self_teaching_rule() -> str:\n"
            "    principle = \"Read carefully, tinker actively, and build real tools\"\n"
            "    return principle\n"
            "\n"
            "print(self_teaching_rule())\n"
            "# Output: Read carefully, tinker actively, and build real tools"
        ),
        (
            "# 02. The Three Pillars of Autonomy\n"
            "pillars = [\n"
            "    \"1. Slow, symbol-by-symbol reading\",\n"
            "    \"2. Deconstructing problems into functions\",\n"
            "    \"3. Shipping open-source projects\"\n"
            "]\n"
            "for item in pillars:\n"
            "    print(f\"-> {item}\")"
        ),
        (
            "# 03. Python 3.12+ Modern Execution Environment\n"
            "import sys\n"
            "\n"
            "version = f\"{sys.version_info.major}.{sys.version_info.minor}\"\n"
            "print(f\"Active Python Runtime: {version}\")\n"
            "assert sys.version_info >= (3, 12), \"Python 3.12+ is required!\"\n"
            "# Output: Active Python Runtime: 3.12"
        ),
        (
            "# 04. Compound Returns of Daily Deliberate Practice\n"
            "def mastery_growth(days: int = 365, daily_gain: float = 0.01) -> float:\n"
            "    # 1.01 ^ 365 ~= 37.78x improvement per year\n"
            "    return (1.0 + daily_gain) ** days\n"
            "\n"
            "multiplier = mastery_growth()\n"
            "print(f\"1-Year Compound Mastery: {multiplier:.2f}x\")"
        )
    ],

    "01-getting-started": [
        (
            "# 01. Computers are Literal: Every Symbol Matters\n"
            "# Syntax matters: a missing quote or bracket halts execution\n"
            "motto = \"Attention to detail is your primary superpower\"\n"
            "tokens = motto.split()\n"
            "print(f\"Token count: {len(tokens)} -> {tokens[:3]}...\")\n"
            "# Output: Token count: 7 -> ['Attention', 'to', 'detail']"
        ),
        (
            "# 02. Your First Program & Comments\n"
            "def welcome(learner: str) -> str:\n"
            "    # Single line comment explaining logic to future you\n"
            "    return f\"Welcome to Self-Teaching, {learner}!\"\n"
            "\n"
            "message = welcome(\"Pythonista\")\n"
            "print(message)\n"
            "# Output: Welcome to Self-Teaching, Pythonista!"
        ),
        (
            "# 03. Modern f-strings & Debug Expressions\n"
            "framework = \"Python\"\n"
            "version = 3.12\n"
            "is_ready = True\n"
            "\n"
            "# The {var=} syntax prints both the identifier and its value\n"
            "print(f\"{framework=}, {version=}, {is_ready=}\")\n"
            "# Output: framework='Python', version=3.12, is_ready=True"
        ),
        (
            "# 04. Reading Tracebacks with Confidence\n"
            "try:\n"
            "    calculation = 100 / 0\n"
            "except ZeroDivisionError as err:\n"
            "    # Read the bottom line: error type & explanation tell you everything\n"
            "    print(f\"Traceback caught: {type(err).__name__} -> {err}\")\n"
            "# Output: Traceback caught: ZeroDivisionError -> division by zero"
        )
    ],

    "02-values-and-operators": [
        (
            "# 01. Dynamic Typing & Builtin Types\n"
            "count: int = 42\n"
            "price: float = 19.99\n"
            "title: str = \"The Craft of Self-Teaching\"\n"
            "active: bool = True\n"
            "\n"
            "print(type(count), type(price), type(title), type(active))\n"
            "# Output: <class 'int'> <class 'float'> <class 'str'> <class 'bool'>"
        ),
        (
            "# 02. Variables are Name Tags Bound to Objects\n"
            "original_list = [10, 20, 30]\n"
            "alias = original_list  # Both point to the exact same memory address\n"
            "alias.append(40)\n"
            "\n"
            "print(f\"{original_list=}\")  # [10, 20, 30, 40]\n"
            "print(f\"{alias is original_list=}\")  # True"
        ),
        (
            "# 03. Comparison and Logical Operators\n"
            "x, y = 15, 25\n"
            "in_range = (10 <= x < 20)\n"
            "is_valid = in_range and (y > x) and (y != 0)\n"
            "\n"
            "print(f\"{in_range=}, {is_valid=}\")\n"
            "# Output: in_range=True, is_valid=True"
        ),
        (
            "# 04. Explicit Type Conversions\n"
            "raw_value = \"150\"\n"
            "parsed_int = int(raw_value)\n"
            "tax = parsed_int * 0.15\n"
            "\n"
            "print(f\"Parsed: {parsed_int} -> Total with Tax: ${parsed_int + tax:.2f}\")\n"
            "# Output: Parsed: 150 -> Total with Tax: $172.50"
        )
    ],

    "03-control-flow": [
        (
            "# 01. Conditional Logic: if / elif / else\n"
            "score = 88\n"
            "if score >= 90:\n"
            "    rank = \"A (Excellence)\"\n"
            "elif score >= 80:\n"
            "    rank = \"B (Very Good)\"\n"
            "else:\n"
            "    rank = \"C (Keep Practicing)\"\n"
            "\n"
            "print(f\"{score} -> {rank}\")\n"
            "# Output: 88 -> B (Very Good)"
        ),
        (
            "# 02. Loops with break and continue\n"
            "for num in range(1, 10):\n"
            "    if num % 2 == 0:\n"
            "        continue  # Skip even numbers\n"
            "    if num > 7:\n"
            "        break     # Terminate loop early\n"
            "    print(f\"Odd candidate: {num}\")"
        ),
        (
            "# 03. Modern Structural Pattern Matching (match/case)\n"
            "def execute(command: str) -> str:\n"
            "    match command.split():\n"
            "        case [\"start\"]:\n"
            "            return \"Engine initialized\"\n"
            "        case [\"go\", (\"north\" | \"south\" | \"east\" | \"west\") as direction]:\n"
            "            return f\"Moving towards {direction}\"\n"
            "        case _:\n"
            "            return \"Command unrecognized\"\n"
            "\n"
            "print(execute(\"go north\"))"
        ),
        (
            "# 04. The Classic FizzBuzz Algorithm\n"
            "for n in range(1, 16):\n"
            "    match (n % 3 == 0, n % 5 == 0):\n"
            "        case (True, True): print(\"FizzBuzz\", end=\" \")\n"
            "        case (True, False): print(\"Fizz\", end=\" \")\n"
            "        case (False, True): print(\"Buzz\", end=\" \")\n"
            "        case _: print(n, end=\" \")"
        )
    ],

    "04-data-structures": [
        (
            "# 01. Lists (Mutable) vs Tuples (Immutable)\n"
            "languages = [\"Python\", \"Rust\"]\n"
            "languages.append(\"Go\")      # Lists can be modified\n"
            "\n"
            "coordinates = (24.7136, 46.6753)  # Tuples are fixed in stone\n"
            "print(f\"{languages=}, {coordinates=}\")"
        ),
        (
            "# 02. Dictionaries for Fast Key-Value Lookups\n"
            "profile = {\n"
            "    \"username\": \"zeiad6\",\n"
            "    \"role\": \"Engineer\",\n"
            "    \"badges\": [\"Python 3.12\", \"Self-Learner\"]\n"
            "}\n"
            "print(f\"User: {profile['username']} | Badges: {len(profile['badges'])}\")"
        ),
        (
            "# 03. Sets: Fast Membership & Math Operations\n"
            "backend = {\"Python\", \"FastAPI\", \"PostgreSQL\"}\n"
            "cloud = {\"Docker\", \"Python\", \"GitHub Actions\"}\n"
            "\n"
            "overlap = backend & cloud  # Set intersection\n"
            "print(f\"Shared technologies: {overlap}\")"
        ),
        (
            "# 04. Expressive List & Dict Comprehensions\n"
            "numbers = [1, 2, 3, 4, 5, 6, 7, 8]\n"
            "even_squares = [x**2 for x in numbers if x % 2 == 0]\n"
            "square_map = {x: x**2 for x in numbers[:4]}\n"
            "\n"
            "print(f\"{even_squares=}\")\n"
            "print(f\"{square_map=}\")"
        )
    ],

    "05-functions": [
        (
            "# 01. Decomposing Problems with Pure Functions\n"
            "def calculate_subtotal(items: list[float]) -> float:\n"
            "    return sum(items)\n"
            "\n"
            "def apply_discount(subtotal: float, rate: float = 0.10) -> float:\n"
            "    return subtotal * (1.0 - rate)\n"
            "\n"
            "print(f\"Final total: ${apply_discount(calculate_subtotal([50, 30, 20])):.2f}\")"
        ),
        (
            "# 02. Type Annotations & Clear Docstrings\n"
            "def summarize(title: str, views: int) -> str:\n"
            "    \"\"\"Format chapter summary stats with clean metrics.\"\"\"\n"
            "    return f\"{title}: {views:,} views\"\n"
            "\n"
            "print(summarize(\"Functions & Scope\", 14500))"
        ),
        (
            "# 03. Variadic Arguments (*args and **kwargs)\n"
            "def dispatch_event(event_type: str, *tags, **metadata):\n"
            "    print(f\"[{event_type}] Tags: {tags}\")\n"
            "    for key, val in metadata.items():\n"
            "        print(f\"   - {key}: {val}\")\n"
            "\n"
            "dispatch_event(\"DEPLOY\", \"v1.2\", \"prod\", author=\"ziad\", ci=True)"
        ),
        (
            "# 04. Memory-Efficient Generators with yield\n"
            "def fibonacci(limit: int):\n"
            "    a, b = 0, 1\n"
            "    while a < limit:\n"
            "        yield a\n"
            "        a, b = b, a + b\n"
            "\n"
            "print(\"Fibonacci sequence:\", list(fibonacci(50)))"
        )
    ],

    "06-strings-and-regex": [
        (
            "# 01. Essential String Operations\n"
            "raw_text = \"   the craft of self-teaching   \"\n"
            "cleaned = raw_text.strip().title()\n"
            "words = cleaned.split()\n"
            "\n"
            "print(f\"Clean: '{cleaned}'\")\n"
            "print(\"Joined with arrows:\", \" -> \".join(words))"
        ),
        (
            "# 02. Advanced Number and Currency Formatting\n"
            "total_revenue = 1845720.456\n"
            "print(f\"Financial Balance: ${total_revenue:,.2f}\")\n"
            "\n"
            "completion_ratio = 0.942\n"
            "print(f\"Curriculum Progress: {completion_ratio:.1%}\")"
        ),
        (
            "# 03. Regex Pattern Matching & Extraction\n"
            "import re\n"
            "\n"
            "email_pattern = re.compile(r\"^([\\w\\.-]+)@([\\w\\.-]+\\.\\w+)$\")\n"
            "match = email_pattern.match(\"learner@selfteaching.org\")\n"
            "\n"
            "if match:\n"
            "    user, domain = match.groups()\n"
            "    print(f\"Verified: User='{user}' on Domain='{domain}'\")"
        ),
        (
            "# 04. Pattern Substitution and Sanitization\n"
            "import re\n"
            "\n"
            "log_line = \"Confidential: user1@corp.com sent token to user2@corp.com\"\n"
            "anonymized = re.sub(r\"[\\w\\.-]+@\", \"[REDACTED]@\", log_line)\n"
            "\n"
            "print(\"Sanitized Audit Log:\")\n"
            "print(anonymized)"
        )
    ],

    "07-file-io": [
        (
            "# 01. Modern Filesystem Operations with pathlib\n"
            "from pathlib import Path\n"
            "\n"
            "workspace = Path(\"project_data\")\n"
            "workspace.mkdir(exist_ok=True)\n"
            "\n"
            "config_file = workspace / \"settings.txt\"\n"
            "config_file.write_text(\"theme=dark\\nauto_save=true\", encoding=\"utf-8\")\n"
            "print(f\"Wrote config to: {config_file.resolve()}\")"
        ),
        (
            "# 02. Context Managers for Safe Resource Management\n"
            "from pathlib import Path\n"
            "\n"
            "target = Path(\"records.log\")\n"
            "with open(target, \"a\", encoding=\"utf-8\") as f:\n"
            "    f.write(\"EVENT: Backup executed successfully\\n\")\n"
            "\n"
            "# File automatically flushed and closed even if errors occur\n"
            "print(f\"File size: {target.stat().st_size} bytes\")"
        ),
        (
            "# 03. Structured Data Persistence with JSON\n"
            "import json\n"
            "\n"
            "payload = {\n"
            "    \"app\": \"Craft of Self-Teaching\",\n"
            "    \"version\": \"3.12\",\n"
            "    \"chapters_completed\": 13\n"
            "}\n"
            "serialized = json.dumps(payload, indent=2)\n"
            "print(\"Serialized JSON Output:\\n\" + serialized)"
        )
    ],

    "08-oop": [
        (
            "# 01. Classes and Instance Construction\n"
            "class Course:\n"
            "    def __init__(self, title: str, instructor: str):\n"
            "        self.title = title\n"
            "        self.instructor = instructor\n"
            "\n"
            "book = Course(\"The Craft of Self-Teaching\", \"Li Xiaolai\")\n"
            "print(f\"Active Study: {book.title} ({book.instructor})\")"
        ),
        (
            "# 02. Inheritance and Clean Polymorphism\n"
            "class Shape:\n"
            "    def area(self) -> float:\n"
            "        raise NotImplementedError\n"
            "\n"
            "class Circle(Shape):\n"
            "    def __init__(self, radius: float):\n"
            "        self.radius = radius\n"
            "    def area(self) -> float:\n"
            "        return 3.14159 * (self.radius ** 2)\n"
            "\n"
            "print(f\"Circle Area (r=5.0): {Circle(5.0).area():.2f}\")"
        ),
        (
            "# 03. Modern @dataclass in Python 3.12+\n"
            "from dataclasses import dataclass\n"
            "\n"
            "@dataclass\n"
            "class ChapterSummary:\n"
            "    number: int\n"
            "    title: str\n"
            "    video_rendered: bool = True\n"
            "\n"
            "summary = ChapterSummary(8, \"Object-Oriented Programming\")\n"
            "print(summary)\n"
            "# Output: ChapterSummary(number=8, title='OOP', video_rendered=True)"
        )
    ],

    "09-modules": [
        (
            "# 01. Python Standard Library Batteries Included\n"
            "import math\n"
            "import datetime\n"
            "import statistics\n"
            "\n"
            "grades = [92, 85, 96, 88, 94]\n"
            "print(f\"Mean Score: {statistics.mean(grades)}\")\n"
            "print(f\"Timestamp: {datetime.date.today()}\")\n"
            "print(f\"Circle Circumference: {2 * math.pi * 10:.2f}\")"
        ),
        (
            "# 02. Modular Architecture & Clean Imports\n"
            "# File: greeter.py -> def say_hello(name: str)\n"
            "# File: main.py    -> from greeter import say_hello\n"
            "def format_greeting(learner: str) -> str:\n"
            "    return f\"Keep shipping projects, {learner}!\"\n"
            "\n"
            "print(format_greeting(\"Software Engineer\"))"
        ),
        (
            "# 03. Isolated Virtual Environments with uv and pip\n"
            "# Quick setup workflow in terminal:\n"
            "# 1. $ pip install uv\n"
            "# 2. $ uv venv && source .venv/bin/activate\n"
            "# 3. $ uv pip install -r requirements.txt\n"
            "print(\"Lightning-fast, isolated, deterministic package management\")"
        )
    ],

    "10-debugging-and-testing": [
        (
            "# 01. Defensive Exception Handling\n"
            "def safe_divide(numerator: float, denominator: float) -> float:\n"
            "    try:\n"
            "        return numerator / denominator\n"
            "    except ZeroDivisionError:\n"
            "        print(\"Warning: Caught division by zero, returning default!\")\n"
            "        return 0.0\n"
            "    finally:\n"
            "        print(\"Operation finished successfully.\")\n"
            "\n"
            "print(safe_divide(10, 2))"
        ),
        (
            "# 02. Structured Logging vs Ephemeral Prints\n"
            "import logging\n"
            "\n"
            "logging.basicConfig(\n"
            "    level=logging.INFO,\n"
            "    format=\"%(levelname)s: %(message)s\"\n"
            ")\n"
            "logging.info(\"System startup complete.\")\n"
            "logging.warning(\"Disk usage at 85% capacity.\")"
        ),
        (
            "# 03. Automated Unit Testing with pytest\n"
            "def is_leap_year(year: int) -> bool:\n"
            "    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\n"
            "\n"
            "assert is_leap_year(2024) is True\n"
            "assert is_leap_year(2023) is False\n"
            "assert is_leap_year(2000) is True\n"
            "print(\"All pytest verification assertions passed!\")"
        )
    ],

    "11-reading-docs": [
        (
            "# 01. Introspection: dir(), help(), and __doc__\n"
            "sample_str = \"Autonomy\"\n"
            "methods = [m for m in dir(sample_str) if not m.startswith(\"_\")]\n"
            "\n"
            "print(f\"str exposes {len(methods)} public methods:\")\n"
            "print(\", \".join(methods[:8]) + \"...\")"
        ),
        (
            "# 02. Inspecting Function Signatures at Runtime\n"
            "import inspect\n"
            "\n"
            "sig = inspect.signature(sorted)\n"
            "print(f\"Official sorted() signature:\")\n"
            "print(f\"  {sig}\")\n"
            "# Notice positional-only '/' and keyword-only '*' flags"
        ),
        (
            "# 03. Navigating docs.python.org Like a Senior Engineer\n"
            "documentation_structure = {\n"
            "    \"1. Tutorial\": \"High-level concepts and basic introduction\",\n"
            "    \"2. Library Reference\": \"Exhaustive standard library APIs and params\",\n"
            "    \"3. Language Reference\": \"Formal grammar and execution semantics\"\n"
            "}\n"
            "for section, purpose in documentation_structure.items():\n"
            "    print(f\"-> {section}: {purpose}\")"
        )
    ],

    "12-beyond-basics": [
        (
            "# 01. The 4-Step Engineering Delivery Loop\n"
            "steps = [\n"
            "    \"1. Minimum Viable Prototype (MVP) that runs\",\n"
            "    \"2. Deconstruct into modular pure functions\",\n"
            "    \"3. Write unit tests with pytest to prevent regression\",\n"
            "    \"4. Package with pyproject.toml and publish on GitHub\"\n"
            "]\n"
            "for step in steps:\n"
            "    print(f\"-> {step}\")"
        ),
        (
            "# 02. Building a Command Line Tool (CLI Mini Project)\n"
            "def task_runner(args: list[str]):\n"
            "    match args:\n"
            "        case [\"add\", item]:\n"
            "            print(f\"Task added: '{item}'\")\n"
            "        case [\"done\", item_id]:\n"
            "            print(f\"Task #{item_id} marked complete!\")\n"
            "        case _:\n"
            "            print(\"Usage: todo [add <item> | done <id>]\")\n"
            "\n"
            "task_runner([\"add\", \"Master Python 3.12+\"])"
        ),
        (
            "# 03. Choosing Your Next Specialization\n"
            "specializations = {\n"
            "    \"Web & API Development\": [\"FastAPI\", \"Django\", \"SQLAlchemy\"],\n"
            "    \"Data Engineering & AI\": [\"Pandas\", \"PyTorch\", \"DuckDB\"],\n"
            "    \"Automation & Cloud\": [\"Docker\", \"GitHub Actions\", \"AWS\"]\n"
            "}\n"
            "for track, stack in specializations.items():\n"
            "    print(f\"🚀 {track}: {', '.join(stack)}\")"
        )
    ]
}
