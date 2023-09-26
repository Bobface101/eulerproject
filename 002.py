num1 = 1
num2 = 2
total = 0
while num2 < 4_000_000:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if num3 % 2 == 0:
        total += num3
print(total)