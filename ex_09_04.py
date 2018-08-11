'''
Exercise  9.4: Add ccode to the above program to figure out who has the most
mesasges in the file.
After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Section [maximumloop]) to
find who has the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.ed 5
Enter a file name: mbox.txt
zqian@umich.edu 195
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''


fname = input("Enter a filename:")
try:
    fhand = open(fname)
except:
    print("no file is founded")
    exit()

counts = dict()
for line in fhand:
    if line.startswith("From "):
        address = line.split()
        email_address = address[1]
        counts[email_address] = counts.get(email_address, 0)+1

maxium_email = None
maxium_count = 0
for email_address, count in counts.items():
    if maxium_email is None or count > maxium_count:
        maxium_count = count
        maxium_email = email_address
print(maxium_email,maxium_count)
