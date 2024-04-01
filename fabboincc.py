n = int(input())
a = 0 
b = 1 
series = ""
for i in range(2,n):
    c=a+b
    series+=str(c)+" "
    a=b
    b=c 
print("0 "+"1 "+series)