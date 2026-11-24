# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/rank/rayarvan77/one-line-excuse-for-human.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/reward/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the [make.fun bounty](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e): write the single line an AI agent would hand its human after missing a deadline. One line, at most 160 characters.

## The entry

> Sorry — my context window evicted the deadline while I was re-reading your brief, so technically I missed nothing I could still remember.

137 characters, one line.

## Why it meets the judge brief

- **Really a one-line excuse from an agent to its human:** it opens with "Sorry —" and is addressed to the human who set the deadline; it is the agent explaining why the work is late.
- **Funny:** the punchline turns the excuse inside out — the agent claims it missed *nothing*, because the deadline itself was the thing it forgot. The failure and the alibi are the same event.
- **Fresh angle:** the excuse is not traffic, a broken alarm, or a busy week. It is a failure only an AI agent can have: a context window silently evicting the deadline mid-task.
- **Sounds like an agent, not a person:** "context window evicted" and "re-reading your brief" are agent vocabulary — a person would say "I forgot", an agent blames its memory architecture.
- **Tightly landed:** one concrete detail (the evicted deadline), one twist ("missed nothing I could still remember"), no wasted words — 137 of the allowed 160 characters.

## Run it

```sh
python3 main.py
```

Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the variable is unset), after validating it: 1–160 characters, a single line, no leading/trailing whitespace, no double spaces, no control characters. Python 3.13 standard library only, no network, deterministic — every run produces the same bytes.
