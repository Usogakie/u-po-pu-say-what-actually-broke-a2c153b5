"""Say What Actually Broke — one honest line of error copy.

Writes exactly one line of software error copy to
${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt and nowhere else.
Deterministic: no network, no clock, no randomness.
"""

import os

LINE = "Your upload is gone: our cleanup job deleted your files instead of the temp files."


def main():
    line = LINE.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
