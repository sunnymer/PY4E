'''
Exercise  10.3: Write a program that reads a file and prints the letters in
decreasing order of frequency. Your program should convert all the input to
lower case and only count the letters a-z. Your program should not count
spaces, digits, puntuaction, or anything other than letters a-z. Find text
samples from several different languages and see how letter frequency varies
between languages. Compare your results with the tables at
wikipedia.org/wiki/Letter_frequencies
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''
fname = input("Enter a filename:")
try:
    fhand = open(fname)
except:
    print("no such file found")
    exit()

words = fhand.read()
words = words.lower()
twords = tuple(words)

letterslist = []
for letters in twords:
    if letters.isalpha() == True:
        letterslist.append(letters)

counts = {}
for letter in letterslist:
    counts[letter] = counts.get(letter,0) + 1

lst = []
for letter, count in counts.items():
    newtup = (count, letter)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for count, letter in lst[:]:
    print(letter, count)
