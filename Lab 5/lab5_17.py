#For loop
for x in range(33, 126, 10):
    for z in range (0,10):
        print(" ", x+z, end = '')
    print()
    for y in range (0, 10):
        if x+y < 100:
            print(" ", chr(x+y), end = ' ')
        else:
            print(" ", chr(x+y), end = '  ')
    print()

#while loop

decimalcode = 33

while decimalcode <= 126:
    i = 0
    j = 0
    while i <= 10:
        print(" ", decimalcode + i, end = '')
        i += 1
    print()
    while j <= 10:
        if j +decimalcode < 100:
            print(" ", chr(decimalcode + j), end = ' ')
        else:
            print(" ", chr(decimalcode + j), end = '  ')
        j += 1
    print()
    decimalcode += 10

