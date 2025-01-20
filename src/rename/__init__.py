#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

import re
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path

parser = ArgumentParser(
    "rename",
    formatter_class=RawDescriptionHelpFormatter,
    description="Rename one or several files or directories with all occurences of substring 'old' replaced by 'new'",
    epilog="""
    Note: Prefer wrapping regular expressions in single quotes to avoid interpretation of the shell

    Examples:

    Replace a simple text on a file
        $ rename --verbose my-file.txt file note
        my-file.txt -> my-note.txt

    Replace a simple text on many files
        $ rename --verbose my-file-1.txt my-file-2.txt file note
        my-file-1.txt -> my-note-1.txt
        my-file-2.txt -> my-note-2.txt

    Replace using a regular expression
        $ rename --verbose 1-my-file-1.txt '\\d' X
        my-file-1.txt -> X-my-file-X.txt

    Replace using a regular expression and capture groups
        $ rename --verbose my-file-1.txt '(.*)-(.)\\.txt' '\\2-\\1.txt'
        my-file-1.txt -> 1-my-file.txt
    """,
)
parser.add_argument("sources", nargs="+", help="One or many paths to files or directories to rename")
parser.add_argument(
    "old",
    help="Substring to replace. It can be a Python regular expression with capture groups",
)
parser.add_argument(
    "new",
    help="Substring replacement. You can use capture groups (e.g: \\1, \\2, ...)",
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Cause rename to be verbose, showing files as they are renamed",
)
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Display new names intead of actually renaming sources",
)


def main():
    args = parser.parse_args()
    regex = re.compile(args.old)

    for source in args.sources:
        source = Path(source)
        if not source.exists():
            print("rename:", f"{source}:", "No such file or directory")
            continue

        old_name = source.name
        new_name = regex.sub(args.new, source.name)
        message = [old_name, "->", new_name]

        if args.dry_run:
            message.insert(0, "[DRY RUN]")
        else:
            source.rename(source.with_name(new_name))
        if args.verbose or args.dry_run:
            print(*message)


if __name__ == "__main__":
    main()
