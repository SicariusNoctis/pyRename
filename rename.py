import sys
import os
import re
import argparse

argsParser = argparse.ArgumentParser(description='Regex rename utility')
argsParser.add_argument('-f', action="store", required=True, help="Find regex")
argsParser.add_argument('-r', action="store", required=True, help="Replace regex (use \1, \2, ... for captures)")
args = argsParser.parse_args()

path = "."
find = args.f
replace = args.r
regexOptions = re.IGNORECASE

print("\nFind: %s\nReplace: %s" % (find, replace))

def getRenameList(path: str, find: str, replace: str, regexOptions=re.IGNORECASE):
	fnames = os.listdir(path)
	regex = re.compile(find, regexOptions)

	return [(f, regex.sub(replace, f)) for f in fnames if regex.match(f)]

# Get conflicts in duplicate outputs
def getDuplicateConflicts(renameList):
	newNames = [x[1] for x in renameList]
	return [x for x in renameList if newNames.count(x[1]) > 1]

# Find conflicts with existing files
def getExistingConflicts(renameList, path):
	fnames = os.listdir(path)
	newNames = [x[1] for x in renameList]

	return [f for f in fnames if f in newNames]

def renameFiles(renameList):
	[os.rename(x[0], x[1]) for x in renameList]

def prettyPair(pairs, middle):
	return "\n".join([("{0}" + middle + "{1}").format(*x) for x in pairs])

renameList = getRenameList(path, find, replace, regexOptions)
duplicateConflicts = getDuplicateConflicts(renameList)
existingConflicts = getExistingConflicts(renameList, path)

print("\n\nReplacements:\n" + prettyPair(renameList, " => "))
print("\n\nConflicts (duplicate output):\n" + prettyPair(duplicateConflicts, " => "))
print("\n\nConflicts (with existing files):\n" + "\n".join(existingConflicts))

if input("\n\nContinue with rename? [Y/N]").upper() == "Y":
	renameFiles(renameList)
