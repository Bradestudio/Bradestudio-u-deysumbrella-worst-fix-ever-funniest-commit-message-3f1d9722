# Worst Fix Ever: Funniest Commit Message — make.fun bounty entry

[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Bradestudio/Bradestudio-u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Bradestudio/Bradestudio-u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

## The entry

> fix: cache the login page — now everyone logs in as Dave

56 characters, one line.

## Why it works

The fix is plausible: cache the login page to speed it up. The backfire is specific and absurd: the cache serves one session to everyone, so every user is now logged in as the same person — Dave. It reads exactly like a commit subject a tired engineer would type at the end of a bad day, and the joke lands on its own in one read, with no explanation needed. It avoids the obvious angles (no revert, no testing in production, no "broke everything") and the punchline is a concrete image, not a complaint.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the text — exactly one line, non-blank, 1–100 characters, no leading/trailing whitespace, opening as a `fix:` commit and ending with the backfire that everyone logs in as Dave — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```
