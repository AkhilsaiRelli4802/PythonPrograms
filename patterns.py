n = int(input())

# Star Pattern
for i in range(1,n+1):
    print("*"*i)

# Number pattern 
for i in range(1,n+1):
    print(str(i)*i)

# 1
# 12
# 123
# 1234

for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    print()

# inclined triangle
    
for i in range(1,n+1):
    print("*"*(n-i+1))

# inclined nums 
for i  in range(1,n+1):
    for j in range(n-i+1):
        print(j+1,end="")
    print()

# Pyramid 
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)