# 📎 Appendix A: Modern Development Setup (VS Code + JupyterLab + Python 3.12+)

## 1. Install Python 3.12+
- **Windows:** download from [python.org](https://www.python.org/downloads/) and tick **Add python.exe to PATH**, or run `winget install Python.Python.3.12`.
- **macOS:** `brew install python@3.12`
- **Linux:** use your distro's package manager or `pyenv`.

Verify:
```bash
python --version
```

## 2. Virtual Environment & Requirements
```bash
git clone https://github.com/zeiad6/craft-of-selfteaching.git
cd craft-of-selfteaching

# Classic way
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
```

### Faster alternative: `uv`
```bash
pip install uv
uv venv
uv pip install -r requirements.txt
```

## 3. VS Code
1. Install [VS Code](https://code.visualstudio.com/).
2. Install the **Python**, **Jupyter**, and **Pylance** extensions (all by Microsoft). **Ruff** is recommended for formatting and linting.
3. Open the folder, press `Ctrl+Shift+P`, choose **Python: Select Interpreter**, and pick `.venv`.
4. Open any `.ipynb`, pick the Kernel at the top right, and run a cell with `Shift+Enter`.

Handy shortcuts: `Ctrl+Shift+P` command palette, `F5` run with debugger, `F9` toggle breakpoint.

## 4. JupyterLab
```bash
jupyter lab
```
- `Shift+Enter` runs a cell; `Esc` then `A`/`B` adds a cell above/below; `M` converts to Markdown; `Y` to code.
- **Kernel → Restart Kernel and Run All Cells** proves the notebook runs top to bottom from scratch.
- **View → Show Table of Contents** displays the notebook outline.

## 5. Google Colab (zero setup)
Open a notebook via its **Open in Colab** badge. The code in this book runs as-is, and Colab usually provides a recent Python. Check with:
```python
import sys; print(sys.version)
```

## 6. Troubleshooting
| Problem | Fix |
| :-- | :-- |
| `python` not recognized | Reinstall with PATH enabled, or try `py` on Windows |
| Can't activate `.venv` in PowerShell | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| Kernel missing in VS Code | `pip install ipykernel` inside the virtual environment |
| Garbled Arabic when reading files | Pass `encoding="utf-8"` when opening files |

---
[🏠 English Index](../README.md) | [Appendix B: Git & GitHub ➡️](./02-git-basics.md)
