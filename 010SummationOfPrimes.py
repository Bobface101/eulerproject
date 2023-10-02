import math

Primes = [2]
num = 3
for num in range(3, 2_000_000,2):
    composite = False
    sqrt = math.sqrt(num)
    for factor in Primes:
        if factor <= sqrt:
            if num % factor == 0:
                composite = True
        else:
            break
    if composite == False:
        Primes.append(num)
print(Primes, sum(Primes))
