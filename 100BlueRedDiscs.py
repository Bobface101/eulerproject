"""
Problem 100:
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, 
and two discs were taken at random, it can be seen that the probability of taking two blue discs, 
P(BB) = (15/21) · (14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blues discs at random,
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 discs in total, 
determine the number of blue discs that the box would contain.
"""




def solution(n: int) -> float:
    return (0.5 + ((4 + 8*(n**2) - 8*n)**0.5)/4)


for n in range(int(10**12), int(10**13)):
    b = solution(n)
      
    if b.is_integer() and (b/n)*((b-1)/(n-1)) == (0.5):
        print(n, b)
        

"""
n, b = 1000153591841, 707215387019
r = n -b
print(r)
print(b + r > 10*12)
print(b/n)
print((b-1)/(n-1))
print((b/n)*((b-1)/(n-1)))
"""

def brahmaguptaComposition(p1, p2):
    pass
#use brahmaguptas identity to recursively generate new solutions usng the first 2 points given

""""""



