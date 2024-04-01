#extract digits from the string
mystring = "Maintaining 12345 & expending 12345 the database of prospects for 12345 the org"
digits=""
for i in mystring:
    if i.isdigit():
        digits+=i
print(digits)