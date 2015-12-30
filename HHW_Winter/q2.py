string1 = raw_input("Enter string to check for palindrome :")       #Take string input
string1 = string1.lower()                                           #Never trust your user ;)
string2 = ""                                                        #Blank string to hold reversed string
length = len(string1)                                               #Counter variable
for a in range(-1,(-length-1),-1):                                  #Reverse indexing loop, will create reversed string. -1 has been done because range() does not take upper limit
    string2+=string1[a]                                             #Make the reversed string
if string1==string2:                                                #Check for plaindrome
    print string1,"is a palindrome"
else:
    print string1,"is not a palindrome"
