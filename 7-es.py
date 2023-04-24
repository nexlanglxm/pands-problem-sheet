letter = 'e'

import os
if os.path.exists("/mobydick.txt"):
    with open(FILENAME, "rt") as f:
        for line in f:
            print(line, end='')
else:
    print ("/mobydick.txt", "does not exist")

with open("/mobydick.txt", 'rt') as f:
    # read all lines in a list
    lines = f.read()
    if line.find(letter) != -1:
            print(letter, 'exists in file')

print("/mobydick.txt".count(letter))