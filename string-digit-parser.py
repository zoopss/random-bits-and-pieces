string =  raw_input('Enter a alphanumeric string...')
total = 0
digits = []
for i in string :
    if i.isalpha():
        pass
    else:
        i = int(i)
        total += i
        digits.append(i)
if total == 0:
    print "The string has no digits"
else:
    print "The original string is :", string
    print "The digits are :", digits
    print "The total of the given digits is :", total
