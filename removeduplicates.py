mylist = [2,5,7,5,3,4,5,2] 
uniquevaluelist = [] 
for i in mylist:
    if i not in uniquevaluelist:
        uniquevaluelist.append(i)
print(uniquevaluelist)