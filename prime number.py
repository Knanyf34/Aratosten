import math
num = int(input())
digits = int(math.log10(num))
first_digit = int(num / pow(10, digits))

while (num >= 10):
    num = num // 10
print('The first digit of number:', first_digit)