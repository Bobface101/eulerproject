"""The following iterative sequence is defined for the set of positive integers:

 n = n / 2
 (n is even)
 
 
 n = 3n + 1
 
 (n is odd)

It can be seen that this sequence (starting at 13 and finishing at 1) contains 8 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at .

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""
from tqdm import tqdm 

nums = []
maxcount = 0

def collatz(number):
    ognum = number
    count = 0
    while True:
        if number % 2 == 0:
            number /= 2
            count += 1
        else:
            number = 3*number + 1
            count += 1
        if number == 1:
            nums.append([ognum,count])
            break

for number in tqdm(range(1, 1_000_001)):   
    collatz(number)

for pair in nums:
    if pair[1] > maxcount:
        maxcount = pair[1]
        print(pair)

        