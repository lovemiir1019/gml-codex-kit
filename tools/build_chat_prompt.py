"""Build the ready-to-paste Chat prompt from the same rules used by Codex."""

from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "gml-gamemaker"
TARGET = ROOT / "chat" / "START_HERE.md"


def build() -> str:
    paths = [
        ROOT / "chat" / "chat-mode.md",
        SKILL / "references" / "gml-rules.md",
        SKILL / "assets" / "HANDOFF_TEMPLATE.md",
    ]
    parts = [path.read_text(encoding="utf-8-sig").strip() for path in paths]
    return "\n\n---\n\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    expected = build()
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding="utf-8-sig") != expected:
            print("Chat prompt is missing or out of date.")
            return 1
        print("Chat prompt matches the shared GML rules.")
        return 0
    TARGET.write_text(expected, encoding="utf-8", newline="\n")
    print("Built chat/START_HERE.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
