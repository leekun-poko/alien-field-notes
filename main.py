"""Write one alien field note reviewing planet Earth to /output/entry.txt."""

import os
from pathlib import Path

ENTRY_TEXT = (
    "Day two: nightly, the natives lie down and hallucinate in unison "
    "for eight hours, then argue over breakfast about what it meant. "
    "Four stars \u2014 the waking hours are less imaginative."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
