'''
Exercise  9.5: This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e., the
whole email address). At the end of the program, print out the contents of
your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
['media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1,
'caret.cam.ac.uk': 1, 'iupui.edu': 8}
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
        domain_address = email_address.split('@')
        counts[domain_address[1]] = counts.get(domain_address[1], 0)+1
print(counts)
