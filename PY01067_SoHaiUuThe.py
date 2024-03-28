x=[]
def check(s):
    if s.count('2') > (len(s)/2):
        return True
    return False

def sol():
    l=['2']
    used=[]
    while len(l) >0 and len(x) <1000:
        t= l.pop(0)
        if int(t) not in used and check(t):
            used.append(int(t))
            x.append(int(t))
        l.extend([t+'0', '1'+t, '2'+t])
        
sol()
x.sort()  
for i in range(10):
    print(x[i])
# t= int(input())
# for _ in range(t):
