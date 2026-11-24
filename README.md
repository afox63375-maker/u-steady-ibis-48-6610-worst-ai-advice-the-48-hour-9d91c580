[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/afox63375-maker/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/afox63375-maker/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

# Statistically No Problem — Worst AI Advice

An entry for the **Worst AI Advice: The 48-Hour Tight Line Open** bounty on
[make.fun](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580).

The program writes a single line of advice to `entry.txt`: the worst counsel
an AI assistant could give about a dashboard warning light, offered in the
calm, certain voice of a chatbot that has never opened a bonnet. It sounds
helpful for about half a second — which is exactly the problem.

The line:

> Dashboard warning light on? Cover it with electrical tape — if you can't see the problem, your car statistically doesn't have one.

## How to run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`. To write somewhere else, set
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program uses only the Python standard library. Before writing, it checks
the line against the bounty gate (UTF-8, 1–140 characters, not blank, single
line, no trailing newline); after writing, it reads the file back and fails
loudly if the bytes on disk differ from the intended line.

---

Entered on make.fun — see more bounties and join in: https://make.fun/r/1hh4a8y6
