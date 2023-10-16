"""What is the sum of the digits of the number 2^1000"""
from tqdm import tqdm

num = 2**1000
sum = 0
for char in tqdm(str(num)):
    sum += int(char)
print(sum)