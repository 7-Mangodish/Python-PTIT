with open('VANBAN.in') as f:
    lines = f.read()
w = lines.split()

def check(x):
    l =0
    r = len(x) -1
    while l<r:
        if x[l] != x[r]:
            return False
        l+=1
        r-=1
    return True

d = dict()
g = 0
for i in w:
    if check(i):
        if i not in d.keys():
            d[i] = 1
            g = max(g, len(i))
        else:
            d[i] = d[i] +1

for i in d.keys(): 
    if len(i) ==  g:
        print(i, d[i])