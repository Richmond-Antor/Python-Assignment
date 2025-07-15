set1 = set(map(int, input("Enter numbers for set 1 : ").split()))
set2 = set(map(int, input("Enter numbers for set 2 :").split())) 
print("set 1 :",set1)
print("set 2 :",set2)

union_set= set1.union(set2)
print(" After union: ",union_set)

intersec_set = set1.intersection(set2)
print(" After intersection: ",intersec_set)

difference_set= set1.difference(set2)
print(" After difference set1 - set2: ",difference_set)

difference_set= set2.difference(set1)
print(" After difference set2 - set1: ",difference_set)