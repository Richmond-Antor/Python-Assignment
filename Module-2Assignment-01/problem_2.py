#Problem: 02

#Write a function that sorts a list of strings alphabetically. 

#["apple", "banana", "cherry", "kiwi", "grape"]

def myfunc(mylist):
    mylist.sort()
mylist=["apple", "banana", "cherry", "kiwi", "grape"]
print("Before sorting:",mylist)
myfunc(mylist)
print("after sorting :",mylist)
