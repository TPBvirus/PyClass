#Thomas Bercasio
#8/30/2018
#lab 2

#2.5
total = eval(input("What is your total: "))
percent = eval(input("What is your tip percentage: "))
tip = total * ( percent / 100 )
subtotal = tip + total

print("Your tip is: " + str(tip))
print("Your subtotal is: " + str(subtotal))

