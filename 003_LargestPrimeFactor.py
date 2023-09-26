import math
from tqdm import tqdm
CONST_NUM = 600851475143
"""
# generate primes until 1/2 of CONST_NUM
# check through array if CONST_NUM % prime = 0
# end search when array is complete
primes = [2]
for num in tqdm(range(3,1_000_000)):
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