"""Fridge Roast: One Line, Biggest Laugh.

Stdlib only. Prints nothing fancy: it writes a single roast line
(at most 200 characters) to the entry file the harness reads:

- $ENTRY_OUT, when set, as a file -- or as a directory, in which
  case entry.txt is written inside it;
- $MAKEFUN_OUTPUT_DIR, the kit harness directory, -> entry.txt;
- $ENTRY_OUT_DIR / $OUTPUT, same file-or-directory rule;
- otherwise /output/entry.txt.

The roast: a firmware update turns the fridge into a hostage-taker
that demands a five-star review before it releases the milk.
"""

import os
from pathlib import Path

ROAST = (
    "My fridge installed a firmware update at 2 a.m. and now holds "
    "the milk hostage until I leave it a five-star review."
)

MAX_CHARS = 200


def _file_inside(raw: str) -> Path:
    """Treat an env value as a file path, or a directory holding entry.txt."""
    target = Path(raw)
    if target.is_dir() or target.suffix != ".txt":
        return target / "entry.txt"
    return target


# Where the harness may point us, in priority order. A plain directory
# value always means "<dir>/entry.txt"; MAKEFUN_OUTPUT_DIR is always a
# directory, even before it exists.
DESTINATION_VARS = ("ENTRY_OUT", "MAKEFUN_OUTPUT_DIR", "ENTRY_OUT_DIR", "OUTPUT")


def entry_destination() -> Path:
    """Pick where entry.txt goes, first set variable wins."""
    for name in DESTINATION_VARS:
        value = os.environ.get(name)
        if not value:
            continue
        if name == "MAKEFUN_OUTPUT_DIR":
            return Path(value) / "entry.txt"
        return _file_inside(value)
    return Path("/output/entry.txt")


def roast_line() -> str:
    """The single roast line, checked against the 200-character gate."""
    line = ROAST.strip()
    if not line:
        raise ValueError("roast line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"roast line is {len(line)} chars, over {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    return line


def emit() -> Path:
    """Write the roast to its destination and return the path written."""
    line = roast_line()
    dest = entry_destination()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {dest}")
    return dest


if __name__ == "__main__":
    emit()
