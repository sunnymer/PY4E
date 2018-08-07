'''Exercise  8.1: Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list
that contains all but the first and last elements.
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance'''

def chop(l):
    del(l[0])
    del(l[-1])

def middle(l):
    del(l[0])
    del(l[-1])
    return(l)

list1 = [1,2]
list2 = [1,2]
list3 = [1,2,3]
list4 = [1,2,3]
list5 = [1,2,3,4]
list6 = [1,2,3,4]
middlelist1 = middle(list1)
choplist1 = chop(list2)
middlelist2 = middle(list3)
choplist2 = chop(list4)
middlelist3 = middle(list5)
choplist3 = chop(list6)
print(choplist1, middlelist1,choplist2,middlelist2,choplist3,middlelist3)
