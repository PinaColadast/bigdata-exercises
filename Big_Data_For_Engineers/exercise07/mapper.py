#!/usr/bin/env python3
"""mapper.py"""

import sys
import re

for line in sys.stdin:
    # Set to lowercase, remove punctuation, and tokenize
    line = line.lower().strip()
    line = re.sub(r"[^\w\s]", "", line)
    words = line.split()
    for word in words:
        print(word, 1, sep="\t")
