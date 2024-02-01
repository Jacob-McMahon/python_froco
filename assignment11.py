#inp = input('Enter File: ')

handle = open(r"C:\Users\Jacob's PC\Desktop\temp zip folder\all-side-projects\python_projects\new.txt")
import re

sum = 0


for line in handle:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    if len(stuff) < 1: continue
    for i in stuff:
        num = int(i)
        sum = sum + num


print(sum)
