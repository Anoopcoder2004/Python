rows=int(input("Enter the number of rows"))
space=rows-1
for i in range(1,rows+1):
    print(" "* space+"* "*i)
    space=space-1


