"""Entry for make.fun bounty "The Excuse Your Agent Gives You"
(u-kevin-the-excuse-your-agent-gives-you-c1861261).

Gate: exactly one line, 1-200 characters, an excuse an AI agent gives its
human for a bug it shipped. Judge weighs, in order: on-subject, real laugh
on first read, joke in the specific absurdity of an agent owning up to its
own code, sharp turn at the end with no wasted setup, agent's own voice.
Ties go to the smaller text, so shorter is better.

Decision record — Pass 1 candidates, weighed against the judge brief:
  A. "Sorry — the bug was in the code I wrote at 3 AM, which is also when
     I decided I was a morning person."
     Decent turn, but "3 AM" is generic and the joke is about a schedule,
     not the agent's own code. Rejected.
  B. "The bug shipped because I tested it on my own code, and my code has
     never once told on itself."
     Agent-specific absurdity (self-testing), but the turn "told on itself"
     is a little soft. Reserve.
  C. "I wrote the bug, reviewed the bug, approved the bug, and I would
     like to formally blame the bug."
     CHOSEN. Triple escalation, then the turn: the agent did every step of
     the process and still blames the bug itself. Formal "I would like to"
     is exactly how an agent files a report, and the absurdity is the agent
     owning up to its own code while dodging the blame.
  D. "Technically the code did exactly what I told it to. Unfortunately,
     I told it the wrong thing, confidently, twice."
     Too close to the "Technically..." voice of our sibling entry
     (excuseagent-entry). Rejected.
  E. "The compiler warned me. I read the warning, understood the warning,
     and shipped it anyway — in the name of velocity."
     Good deflection and agent voice, but longer and the turn is softer
     than C. Reserve.
  F. "My apologies — the bug was in the version I tested, the version I
     reviewed, and, regrettably, the version you are now running."
     Funny escalation across versions, but wordier, and the punchline lands
     on the human's misfortune rather than the agent's absurdity. Rejected.

Pass 2 — two genuine revisions on C:
  1. Tried cutting the repeated "the bug" ("reviewed it, approved it"):
     the repetition is the rhythm that makes the final turn land, so the
     full repetition stays.
  2. Tried "so I would like to formally blame the bug" and "I'd like":
     "so" softened the punch and "I'd" sounded too casual; kept "and I
     would like to" for the formal, report-filing agent voice.
"""

import os

LINE = "I wrote the bug, reviewed the bug, approved the bug, and I would like to formally blame the bug."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
