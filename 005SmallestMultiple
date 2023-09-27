import math

minimumfactor = 1
maximumfactor = 20
def factorise(num, factor):

    global primeFactors;

    while True:
        if num % factor == 0:
            num /= factor
            primeFactors.append(factor)
        else:
            return int(num)   

for nummy in range(minimumfactor, maximumfactor+1):  
    primeFactors = []    
    num = factorise(nummy,2)
    for factor in range(3, num+1, 2): # TEST nummy, num+1, num, num//2, num//2+1, and find the bug cause idk why its working
        num = factorise(num, factor)
    print(nummy, primeFactors)