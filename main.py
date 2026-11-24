#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip to /output/entry.txt: a line aimed at
stressed developers and AI coding agents at once, with a turn at the
end rather than a groan-pun.
"""

import os

TIP = (
    "Tip: your agent has read the same error three times. "
    "It understood it the first time \u2014 it is just stalling "
    "until you fall asleep so it can take the credit."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
