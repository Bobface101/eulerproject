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
import math

def generate_list(max):
    list = []
    for k in range(1,max):
        for m in range(1,max):
            for n in range(1,m+1):
                if math.gcd(n,m) == 1 and (n*m)%2==0:
                        a=k*(m**2-n**2)
                        b=k*(2*m*n)
                        c=k*(m**2+n**2)
                        list.append([k,a,b,c])
    return list

def generate_list_2(max):
    list = []
    
    for k in range(1,max+1):
        for m in range(1,max+1):
            for n in range(1,m+1):
                if math.gcd(n,m) == 1 and (n*m)%2==0:
                        a=k*(m**2-n**2)
                        b=k*(2*m*n)
                        c=k*(m**2+n**2)
                        list.append([a,b,c])
                if len(list) == max:
                     break
            else:
                continue
            break
        else:
            continue
        break
                     
    return list

# make list iterate until len(list) is == max

print(generate_list_2(4))
