for x in range(2001, 2101, 50):
    for y in range (0,50):
        z = y+x
        if z % 4 == 0:
            if z % 100 != 0:
                print(z, end = ' ')
    print()

print()

i = 2001
while i <= 2100:
    j = 0
    while j <= 50:
        k = i+j
        if k % 4 == 0:
            if k % 100 != 0:
                print(k , end = ' ')
        j += 1
    print()
    i += 50