FILENAME = "mobydick.txt"
letter = 'e'

import os
if os.path.exists(FILENAME):
    with open(FILENAME, "rt") as f:
        for line in f:
            print(line, end='')
else:
    print (FILENAME, "does not exist")

with open(FILENAME, 'rt') as f:
    # read all lines in a list
    lines = f.read()
    if line.find(letter) != -1:
            print(letter, 'exists in file')

print(FILENAME.count(letter))