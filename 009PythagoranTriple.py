from tqdm import tqdm
for a in tqdm(range(1000)):
    for b in range(1000):
        for c in range(1000):
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print(a,b,c, "product:", (a*b*c))
