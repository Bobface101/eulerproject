import math
from tqdm import tqdm
CONST_NUM = 600851475143

# generate primes until 1/2 of CONST_NUM
# check through array if CONST_NUM % prime = 0
# end search when array is complete

"""
primes = [2]
for num in tqdm(range(3,9999999)):
    composite = False
    for prime in primes:
        if prime < math.sqrt(num):
            if num % prime == 0:
                composite = True
                break
            else:
                pass
    if composite == False:
        primes.append(num)
print(primes)

"""
primeFactors = []
num = 69
while num > 0:
    if num % 2 == 0:
        num /= 2
        primeFactors.append(2)
    elif num == 1:
        break
    else:
        primeFactors.append(num)
        break

print(primeFactors)
