from tqdm import tqdm
import math
Primes = [2]
num = 3
while len(Primes) < 10_0005:
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
    num += 2
print(Primes[10_000])
                
