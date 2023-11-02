"""It turns out that 12cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, 

but there are many more examples.

: 
: 
: 
: 
: 
: 
In contrast, some lengths of wire, like 20cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; 

for example, using  it is possible to form exactly three different integer sided right angle triangles.

: , , 
Given that L is the length of the wire, for how many values of L <= 1_500_000 can exactly one integer sided right angle triangle be formed?"""

from tqdm import tqdm

def generateTriplets(max):
    triplets = []
    for a in tqdm(range(1,max//2)):
        for b in range(1,max//2):
            for c in range(1,max//2):
                if a**2 + b**2 == c**2 and a+b+c < max:
                    triplets.append([a,b,c])
    return triplets

def euclidFormula(max):
    pass