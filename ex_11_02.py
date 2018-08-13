'''
Exercise  11.2: Write a program to look for lines of the form
'New Revision: 39771'
and extract the number from each of the lines using a regular expression and
the findall() method. Compute the average of the numbers and print out the
average.
Enter file:mbox.txt
38549.7949721
Enter file:mbox-short.txt
39756.9259259
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''


import re

fname = input("Enter file:")
try:
    fhand = open(fname)
except:
    print("no such file found!")
    exit()

sum = 0
count = 0
for line in fhand:
    if re.search('^New Revision:',line):
        numbers = re.findall('[0-9]+', line)
        for number in numbers:
            number = float(number)
            count = count + 1
            sum = sum + number
avg = sum / count

print(avg)
