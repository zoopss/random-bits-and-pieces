string = raw_input('Enter string for analysis...')
words = 0
chars = 0
alnum = 0.0
alnum_percent = 0
for a in string:
    chars+=1
    if a.isspace():
        words += 1
    if a.isalnum():
        alnum+=1
alnum_percent = (alnum/len(string)) * 100
print "The number of words in the string are :", words + 1
print "The string has",chars,"characters"
print "The percentage of alphanumeric characters is :",alnum_percent,"%"
    
