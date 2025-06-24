#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program Name: fix_big5_id3.py
Description:
Big5ID3Fixer is a Python program to fix legacy Big5 encoding issues
for ID3 tags in MP3 files created on older Windows systems.
It reads tags that were mis‐decoded as Latin-1 and re-decodes them
properly as Big5/CP950, then saves the corrected Unicode metadata
while preserving original file timestamps.
Author: Adapted for Chinese Big5 by ChatGPT
Last Updated: 2025-06-24
Python Version: 3.10+
License: MIT
"""

import glob
import os
import re
from mutagen.easyid3 import EasyID3

quiet = False


def convert_encoding(input_string):
    """
    Re-decode a Latin-1–decoded Python str as Big5 or CP950.
    """
    try:
        # get back raw bytes
        raw_bytes = input_string.encode('latin1')
    except UnicodeEncodeError:
        # not a Latin-1 mapping ≥ U+0100
        return None

    # try Big5 first, then CP950 as fallback
    for enc in ('big5', 'cp950'):
        try:
            return raw_bytes.decode(enc)
        except UnicodeDecodeError:
            continue

    # give up if neither works
    return None


def fix_big5_tag(id3, tag):
    """
    Attempt to fix one tag by re-decoding it as Big5/CP950.
    Returns True if tag was changed.
    """
    try:
        original = id3[tag][0]
        converted = convert_encoding(original)
        if converted and converted != original:
            if not quiet:
                print(f"  {tag}: {original!r} → {converted!r}")
            id3[tag] = converted
            return True
    except Exception:
        pass
    return False


def fix_big5_encoding(path):
    """
    Load the file’s EasyID3 tags, fix each one, save if any changed,
    and then restore the original atime & mtime.
    """
    try:
        tags = EasyID3(path)
    except Exception as e:
        if not quiet:
            print(f"Skipping {path}: {e}")
        return

    changed = False
    for key in list(tags.keys()):
        if fix_big5_tag(tags, key):
            changed = True

    if changed:
        # capture original timestamps
        stat = os.stat(path)
        orig_atime = stat.st_atime
        orig_mtime = stat.st_mtime

        if not quiet:
            print(f"Updating tags in {os.path.basename(path)}")
        tags.save()

        # restore original timestamps
        os.utime(path, (orig_atime, orig_mtime))


def fix_directory(directory):
    """
    Walk through all MP3s in `directory` (non‐recursive) and fix them.
    """
    # escape any glob metacharacters
    safe_dir = re.sub(r'([\[\]\*\?])', r'[\1]', directory)
    pattern = os.path.join(safe_dir, '*.[mM][pP]3')
    for filepath in glob.glob(pattern):
        if not quiet:
            print(f"Checking {os.path.basename(filepath)}")
        fix_big5_encoding(filepath)


def main():
    root = os.getcwd()
    fix_directory(root)


if __name__ == "__main__":
    main()
