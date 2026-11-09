# 📎 Appendix B: Git & GitHub Essentials for Self-Learners

**Git** records the history of your project; **GitHub** hosts and shares it. A public repository of your projects is the best résumé a self-taught developer can have.

## 1. One-Time Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

## 2. The Core Loop
```bash
git init                      # create a repository
git status                    # what changed?
git add .                     # stage changes
git commit -m "Add chapter 1" # save a snapshot
git log --oneline             # view history
```

## 3. Publishing to GitHub
1. Create an empty **Public** repository on GitHub.
2. Connect it and push:
```bash
git remote add origin https://github.com/zeiad6/craft-of-selfteaching.git
git branch -M main
git push -u origin main
```

## 4. Branches & Pull Requests
```bash
git switch -c feat/new-challenge   # new branch
# ... edit and commit ...
git push -u origin feat/new-challenge
```
Then open a **Pull Request** from the repository page. Tips: one branch per task, and write clear imperative commit messages (`Fix typo in chapter 3`).

## 5. The `.gitignore` File
Never commit your virtual environment or secrets:
```text
.venv/
__pycache__/
.ipynb_checkpoints/
.env
```

> [!WARNING]
> Never put passwords or API keys in a repository. If you push one by accident, treat it as leaked and rotate it immediately.

## 6. Common Fixes
| Situation | Fix |
| :-- | :-- |
| Discard unsaved changes in a file | `git restore file.py` |
| Unstage a file | `git restore --staged file.py` |
| Edit the last commit message | `git commit --amend` |

---
[⬅️ Appendix A](./01-setup-environment.md) | [🏠 English Index](../README.md) | [💡 Challenges ➡️](../challenges/README.md)
