list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
# remove duplicate values 

uniquelist = list(set(list1))

# method1 
uniquelist.sort(reverse=True)
print(uniquelist[1])

# method2 

sortedlist = sorted(uniquelist)
print(sortedlist[-2])