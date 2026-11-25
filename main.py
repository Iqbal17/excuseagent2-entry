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
     CHOSEN (96 characters — well inside the gate; only reserve B is
     shorter, by two characters, and two characters were not worth B's
     softer turn). Triple escalation, then the turn: the agent did every
     step of the process and still blames the bug itself. Formal "I would
     like to" is exactly how an agent files a report, and the absurdity is the agent
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

Pass 3 — structural revision; the line itself was already final, so this
pass reworked only the machinery around it:
  1. The output directory is now resolved by a named helper
     (output_dir) instead of inline in main, so the $MAKEFUN_OUTPUT_DIR
     / /output fallback lives in exactly one documented place.
  2. Added check_line: before writing, the program verifies LINE is
     exactly one line of 1-200 characters and raises otherwise, so a
     future edit to the joke can never silently emit an invalid entry.
  3. Recorded the chosen line's length (96) in the decision record
     above, and corrected the length comparison against the rivals.
  Output behaviour is unchanged: the same single line, written to
  $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output/entry.txt.
"""

import os

LINE = "I wrote the bug, reviewed the bug, approved the bug, and I would like to formally blame the bug."


def output_dir() -> str:
    """Directory the grader reads entry.txt from.

    $MAKEFUN_OUTPUT_DIR when the harness sets it, otherwise /output.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_line(line: str) -> None:
    """Guard the bounty gate: exactly one line, 1-200 characters.

    The chosen line is final, but if anyone ever edits it, this makes the
    program refuse to emit an invalid entry instead of scoring zero.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    check_line(LINE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
