n = int(input()) 
numstring = str(n)
length = len (numstring)
Armstrongnum = 0 
for i in numstring:
    Armstrongnum+=int(i)**length
if n == Armstrongnum:
    print(n," : is Armstrong Num")
else:
    print("Not Armstrong Num")