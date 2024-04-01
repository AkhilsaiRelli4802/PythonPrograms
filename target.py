mylist = [5,8,9,6,3,0]
n=int(input())
for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if (mylist[i]+mylist[j])== n :
            print((mylist[i],mylist[j]))