import math

side = input("What is the length of one side: ")

area = ( ( 3 * math.sqrt(3) ) / 2 ) * math.pow(float(side), 2)

print("Area = %.2f cm^2" % area)