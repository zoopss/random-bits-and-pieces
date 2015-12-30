n = int(raw_input("Enter number of entries to add to phonebook..."))
dict_out={}
for i in range (n):
    key = raw_input("Enter name of person...")
    value = int(raw_input("Enter the number of that person..."))
    dict_out[key]=value
    print "-"*20
while True:
    input1 = raw_input("Enter name to delete from phonebook...")
    if dict_out.has_key(input1):
        dict_out.pop(input1)
        print input1,"and corresponding phone number has been removed"
    else:
        print "Sorry,",input1,"doesn't have a record in this phonebook"
