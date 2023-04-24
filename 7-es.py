letter = 'e'
#to import the os module and check for the file
import os
if os.path.exists("./mobydick.txt"):
    with open("./mobydick.txt", "rt") as f:
        for line in f:
            print(line, end='')
#conditions
else:
    print ("The required file does not exist")

with open("./mobydick.txt", 'rt') as f:
    # read all lines in a list
    lines = f.read()
    if line.find(letter) != -1:
            print(letter, 'exists in file')
#attempting to count out the letters
print("./mobydick.txt".count(letter))