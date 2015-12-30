num1 = int(raw_input("Enter the number of entries to be recorded..."))          #Take counter input
dict1 = {}                                                                      #Create blank dictionary
for i in range(0,num1):                                                         #Loop through to add all entries
    key = raw_input("Enter section name...")                                    #Ask section
    value = raw_input("Enter name of Class Teacher...")                         #Ask Class Teacher
    dict1[key]=value                                                            #Add to the dictionary

print "Current records are \n",dict1                                            #Display result
