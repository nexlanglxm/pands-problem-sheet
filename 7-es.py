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
    for line in lines:
        # check if letter is present on a current line
        if line.find(letter) != -1:
            print(letter, ' exists in file')

print(FILENAME.count("e"))