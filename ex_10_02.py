'''
Exercise  10.2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the "From" line by finding
the time string and then splitting that string into parts using the colon
character. Once you have accumulated the counts for each hour, print out the
counts, one per line, sorted by hour as shown below.
Sample line: From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008
Sample Execution:
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
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
        words = line.split()
        word = words[5]
        timeofday = word.split(":")
        hour = timeofday[0]
        counts[hour] = counts.get(hour,0)+1

lst = []
for hour, count in counts.items():
    newtup = (hour, count)
    lst.append(newtup)

lst = sorted(lst)

for hour, count in lst[:]:
    print(hour, count)
