'''
Exercise  11.1: Write a simple program to simulate the operation of the grep
command on Unix. Ask the user to enter a regular expression and count the
number of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''

import re

input_command = input("Enter a regular expression:")
input_str = str(input_command)
count = 0
hand = open('mbox.txt')

for line in hand:
    line = line.rstrip()
    if re.findall(input_str,line):
        count = count + 1
print("mbox.txt had ",count," lines that matched",input_str)
