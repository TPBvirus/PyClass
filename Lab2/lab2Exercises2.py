num = eval(input("What is your number: "))

first = int(num) % 1000
second = int(num) % 100
third = int(num) % 10
fourth = int(num) % 1

print("%d\n %d\n %d\n %d\n", first, second, third, fourth)