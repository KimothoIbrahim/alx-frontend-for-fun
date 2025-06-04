#!/usr/bin/python3
"""Doc string
"""

from pathlib import Path
import sys


if len(sys.argv) != 3:
    print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
    sys.exit(1)

file = Path(sys.argv[1])

if not file.is_file():
    print(f' Missing {sys.argv[1]}', file=sys.stderr)
    sys.exit(1)

sys.exit()
