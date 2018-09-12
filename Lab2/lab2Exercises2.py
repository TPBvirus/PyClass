num = eval(input("What is your number: "))

first = int(num) % 10
num -= first
first /= 1
second = int(num) % 100
num -= second
second /= 10
third = int(num) % 1000
num -= third
third /= 100
fourth = int(num) % 10000
fourth /= 1000

print("%d\n%d\n%d\n%d\n" % (first, second, third, fourth))
