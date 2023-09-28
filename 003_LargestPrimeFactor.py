import math
from tqdm import tqdm
import time

num = 60085147514383986298360286109876543234567890987654345678909876543456789098765434567876543456789874
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

def factorise(num, factor):

    global primeFactors;

    while True:
        if num % factor == 0:
            num /= factor
            primeFactors.append(factor)
        else:
            return num

time0 = time.time()           
num = factorise(num,2)
for factor in tqdm(range(3, (int(math.sqrt(num))), 2)):
#for factor in tqdm(range(3, (num//2 + 1), 2)):
    num = factorise(num, factor)
print(primeFactors)

time1 = time.time()
finalTime = round(time1-time0,1)
print(f"Time taken: {finalTime}s")

