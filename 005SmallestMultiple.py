from tqdm import tqdm

primeFactors = []    
LCM = [[0,0]]
minimumfactor = 1
maximumfactor = 20
def factorise(num, factor):
#test input with prime number?
    global primeFactors;
    factorcount = 0

    while True:
        if num % factor == 0:
            num /= factor
            factorcount += 1
        elif factorcount > 0:
            primeFactors.append([factor, factorcount])
            return int(num)
        else:
            return int(num)

  
for nummy in tqdm(range(minimumfactor, maximumfactor+1)):
    num = factorise(nummy,2)
    for factor in range(3, num+1, 2): 
        num = factorise(num, factor)

for factorizedNum in tqdm(primeFactors):
    BaseInArray = False
    for num in LCM:
        if factorizedNum[0] == num[0] and factorizedNum[1] > num[1]:
            BaseInArray = True
            LCM.remove(num)
            LCM.append(factorizedNum)
        if factorizedNum[0] == num[0]:
            BaseInArray = True
    if BaseInArray == False:
        LCM.append(factorizedNum)

LCM.remove([0,0])
total = 1
print(LCM)
for num in LCM:
    total *= num[0]**num[1]
print(total)
