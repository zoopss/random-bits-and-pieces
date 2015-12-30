n = int(raw_input("Enter number of entries to add to phonebook..."))            #Take number on entries
dict_out={}                                                                     #Create blank output dict
for i in range (n):                                                             #Keep adding new entries
    key = raw_input("Enter name of person...")
    value = int(raw_input("Enter the number of that person..."))
    dict_out[key]=value
    print "-"*20
while True:                                                                     #Infinite Loop
    name = raw_input("Enter name of person to check database...")               #Input name to check
    if dict_out.has_key(name):                                                  #Check existence
        print name+"\'s number is",dict_out[name]                               #Print number nicely
        print "-"*20
    else:
        print "Sorry we don\'t have",name,"in our records"                      #Default message
        print '-'*20
