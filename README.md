## pyRename

Bulk renames files using specified regexes, and warns about conflicts.

**Installation:**

	python setup.py

**Example usage:**

	python rename.py -f="annoyingPrefix_(.+)" -r="\1"

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

## Todo

 - Ignore directories option
 - Recursive subdirectory rename

## Known issues

 - Renames are not done instantaneously!
