
fname = input('Enter the filename:')
fh = open(fname)

count = 0
total = 0

for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        spos = line.find(':')
        number = line[spos+1:]
        fnumber = float(number)
        total = total + fnumber
        average = total/count

print('average spam confidence value:', average)
