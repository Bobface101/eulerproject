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

sums = []

def generate_triplets(max):
    list = []
    newlist = []
    for m in range(1,max+1):
        for n in range(1,m):
            if math.gcd(n,m) == 1 and (n*m)%2==0:
                    a=(m**2-n**2)
                    b=(2*m*n)
                    c=(m**2+n**2)
                    if a<b:
                        list.append([a,b,c])
                    else:
                         list.append([b,a,c])
            if len(list) == max:
                    break
        else:
            continue
        break
    
    # scale everything up using k
    newlist.append(list)
    for k in range(2,int(math.sqrt(max))): # arbitrary limit
         newlist.append([[j*k for j in i] for i in list])
    newlist = [item for row in newlist for item in row]
    
    newlist.sort()                
    return newlist







def generate_primitive_triplets(max):
    list = []
    for m in range(1,max+1):
        for n in range(1,m):
            if math.gcd(n,m) == 1 and (n*m)%2==0:
                    a=(m**2-n**2)
                    b=(2*m*n)
                    c=(m**2+n**2)
                    if a<b:
                        list.append([a,b,c])
                    else:
                         list.append([b,a,c])
            if len(list) == max:
                    break
        else:
            continue
        break

    list.sort()                
    return list

print(generate_primitive_triplets(1_500_000))


