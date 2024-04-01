n=int(input())
if n >1:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("prime Number :",n)