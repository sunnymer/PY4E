'''Exercise  9.1: Write a program that reads the words in words.txt and stores
them as keys in a dictionary. Download a copy of the file from
https://www.py4e.com/code3/words.txt. It doesn't matter what the values are.
Then use the 'in' operator as a fast way to check whether a string is in the
dictionary.
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''


word_dictionary = dict()
fh  = open("words.txt")
for line in fh:
    words = line.split()
    for word in words:
        word_dictionary[word] = word_dictionary.get(word,0)+1
print('your word dictionary is established!Now you can search!')
find_string = input("Enter a string:")
if find_string in word_dictionary:
  print('we found it!')
else:
  print("the string doesn't exist!")
