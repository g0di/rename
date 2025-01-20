# rename

A small Python script for renaming files and directories using regular expressions.

> I've made this script mostly for my personal usage as I was lacking a tool for quickly renaming lot of files using regular expressions on my personal server.
> If you are in the same situation feel free to use it as well.

## Installation

As I'm not releasing this script on Pypi, the easiest way to install it is through `pipx` or `uv` using this git repository directly.

> Don't forget to ensure that your `pipx` or `uv` installed programs are on your `PATH`

### `pipx`
```bash
pipx install git+https://github.com/g0di/rename/main
```
### `uv`
```bash
uv tool install git+https://github.com/g0di/rename/main
```


## Usage

You can get all the script documentation by simply running `rename --help` with some examples.

```bash
usage: rename [-h] [--dry-run] [-v] sources [sources ...] old new

Rename one or several files or directories with all occurences of substring 'old' replaced by 'new'

positional arguments:
  sources        One or many paths to files or directories to rename
  old            Substring to replace. It can be a Python regular expression with capture groups
  new            Substring replacement. You can use capture groups (e.g: \1, \2, ...)

options:
  -h, --help     show this help message and exit
  -v, --verbose  Cause rename to be verbose, showing files as they are renamed
  --dry-run      Display new names intead of actually renaming sources

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
        $ rename --verbose 1-my-file-1.txt '\d' X
        my-file-1.txt -> X-my-file-X.txt

    Replace using a regular expression and capture groups
        $ rename --verbose my-file-1.txt '(.*)-(.)\.txt' '\2-\1.txt'
        my-file-1.txt -> 1-my-file.txt
```
