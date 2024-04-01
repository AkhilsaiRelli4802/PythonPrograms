mylist = [5,8,9,6,3]

#finding min 
min=mylist[0]
for i in mylist:
    if i<min:
        min=i
print(min)

# finding max
max=mylist[0]
for i in mylist:
    if i>max:
        max=i 
print(max)