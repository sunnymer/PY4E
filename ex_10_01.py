'''
Exercise  10.1: Revise a previous program as follows: Read and parse the "From"
lines and pull out the addresses from the line. Count the number of messages
from each person using a dictionary.
After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the
list in the reverse order and print out the person who has the most commits.
Sample line:
From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''

fname = input("Enter a filename:")
try:
    fhand = open(fname)
except:
    print("no such file found")
    exit()

counts = {}

for line in fhand:
    if line.startswith("From "):
        emails = line.split()
        email_address = emails[1]
        counts[email_address] = counts.get(email_address,0)+1

lst = []
for email_address, count in counts.items():
    newtup = (count, email_address)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for count, email_address in lst[:1]:
     print(email_address, count)
