test_list = [5, 6, [], 3, [], [], 9]
resultlist=[]

for i in test_list:
    if i != []:
        resultlist.append(i)
print(resultlist)