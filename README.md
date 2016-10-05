## pyRename

Bulk renames files using specified regexes, and warns about conflicts.

**Installation:**

	python setup.py install

**Example usage:**

	pyrename -f="annoyingPrefix_(.+)" -r="\1"

**Output:**

	Find: annoyingPrefix_(.+)
	Replace: \1

	Replacements:
	annoyingPrefix_file_1.txt => file_1.txt
	annoyingPrefix_file_2.txt => file_2.txt
	annoyingPrefix_file_3.txt => file_3.txt

	Conflicts (duplicate output):
	None

	Conflicts (with existing files):
	None

	Continue with rename [Y/N]? Y

## Arguments

| Flag | Command          | Description                                      |
| ---- | ---------------- | ------------------------------------------------ |
| -c   | --noconfirmation | Suppress confirmation (if no conflicts)          |
| -d   | --subdirectories | Include subdirectories                           |
| -f   | --find           | Find regex                                       |
| -i   | --ignorecase     | Ignore case                                      |
| -p   | --path           | Directory (default is current directory)         |
| -r   | --replace        | Replace regex (use \\1, \\2, ... for captures)   |
| -w   | --nowarnings     | Suppress warnings                                |

## Todo

 - None

## Known issues

 - Renames are not done instantaneously!
