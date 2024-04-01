mystring = "Maintaining 12345 & expending 12345 the database of prospects for 12345 the org"
dict = {}
for i in mystring:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)