
with open('DATA.in') as f:
    l = f.read()
l = l.split()
def check(s):
    try:
        n = int(s)
    except:
        return True
    else:
        if n >= -(2**31 -1) and n <= (2**31 -1):
            return False
        return True

ans = []
for i in l:
    if check(i):
        ans.append(i)
ans.sort()
print(*ans)