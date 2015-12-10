trrows = int(raw_input("Enter number of rows..."))
tr = trrows/2 + 1
row = 0
for row in range(1,tr+1):
    lnospace=tr - row
    if row == 1:
        print " " * (lnospace+1), "*"
    else:
        print " " * (lnospace),"*"," " * ((2*row - 1) - 2),"*"
for i in range(row,0,-1):
    if i == 1:
        print " " * (lnospace + 1), "*"
    else:
        print " " * lnospace,"*"," " * ((2*i-1)-2),"*"
        lnospace += 1
