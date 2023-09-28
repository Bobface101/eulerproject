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

  
for nummy in range(minimumfactor, maximumfactor+1):
    num = factorise(nummy,2)
    for factor in range(3, num+1, 2): 
        num = factorise(num, factor)

for factorizedNum in tqdm(primeFactors):
    for num in LCM:
        if factorizedNum[0] == num[0] and factorizedNum[1] > num[1]:
            LCM.remove(num)
            LCM.append(factorizedNum)
        if factorizedNum[0] != num[0]:
            LCM.append(factorizedNum)
        else:
            pass
print(LCM)   
print("pipi")