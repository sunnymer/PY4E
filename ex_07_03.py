
fname = input('Enter your filename:')

if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    fh = open(fname)
    count = 0
    for line in fh:
        if line.startswith('subject:'):
            count = count +1

    print('There were', count,'subject lines in ', fname)
