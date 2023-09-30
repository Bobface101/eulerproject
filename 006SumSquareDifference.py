from tqdm import tqdm

def SumOfSquares(start, end):
    total = 0
    for i in tqdm(range(start, end+1)):
        total += i**2
    return total
def SquareOfSum(start, end):
    total = 0
    for i in tqdm(range(start, end+1)):
        total += i
    return total**2

print(SquareOfSum(1,100)-SumOfSquares(1,100))
