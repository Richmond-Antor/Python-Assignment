#Problem: 03

#Write a Python program that creates a new list containing only the duplicate elements from the given list: [1, 5, 6, 5, 1, 2, 3].


oglist=[1, 5, 6, 5, 1, 2, 3]
duplist=[]
for i in oglist:
    if oglist.count(i)>1 and i not in duplist:
        duplist.append(i)



print(duplist)
