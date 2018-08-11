'''
Exercise  9.3: Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from each email
address, and print the dictionary.
Enter file name: mbox-short.txt
{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3,
'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5,
'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1,
'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1,
'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''
fname =input("Enter a filaname:")
try:
    fhand = open(fname)
except:
    print("no such file founded!")
    exit()

ddd = dict()

for line in fhand:
    if line.startswith("From "):
        days = line.split()
        day = days[1]
        ddd[day] = ddd.get(day, 0)+1
print(ddd)
