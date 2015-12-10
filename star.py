trrows=int(raw_input("Enter number of rows:"))
tr = trrows/2 + 1
for row in range(1,tr+1):
    lnospace = tr - row
    if row == 1:
        print " " * (lnospace+1) , "X"
    else:
        print " " * (lnospace), "X", " " * ((2*row-1)-2), "X"
for i in range(row,0,-1):
    if i == 1:
        print " " * (lnospace+1), "X"
    else:
        print " " * (lnospace), "X", " " * ((2*i-1)-2), "X"
        lnospace+=1
