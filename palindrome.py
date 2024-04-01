mystring = input() 
# if given string is equal to the reverse of the string then it said to be palindrome
#reverse a string 
reversestring = mystring[::-1]
if mystring == reversestring:
    print("Palindrome")
else:
    print("Not Palindrome")


# withoutindexing 
    
stringreverse= ""
for i in mystring:
    stringreverse=i+stringreverse
if mystring== stringreverse:
    print("Palindrome")
else:
    print("Not Palindrome")