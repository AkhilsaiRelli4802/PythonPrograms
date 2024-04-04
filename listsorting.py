mylist = [5,8,9,6,3]

# using sort method

mylist.sort()
print(mylist)

#using sorted method

sortedlist = sorted(mylist)
print(sortedlist)

#sorting list in asc order 
mylist.sort(reverse=True)
print(mylist)

#reversing the list 
print(mylist[::-1])

# reversing list 2nd method 
reverlist=[]
for i in mylist:
    reverlist=[i]+reverlist
print(reverlist)