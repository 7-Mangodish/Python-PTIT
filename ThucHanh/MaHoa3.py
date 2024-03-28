
def rotate(s):
    sum = 0
    ans = ''
    for i in s:
        sum += ord(i)-65
    for i in s:
        res = (ord(i) -65 + sum) % 26
        res = chr(res+65)
        ans += res
    return ans

def merge(s1, s2):
    ans= ''
    for i in range(len(s1)):
        res1 = ord(s1[i]) - 65
        res2 = ord(s2[i]) - 65
        res1 = (res1 + res2) % 26
        ans += chr(res1 +65)
    return ans

t = int(input())
for _ in range(t):
    s = input()
    left = s[:len(s)//2]
    right = s[len(s)//2:]

    left = rotate(left)
    right = rotate(right)
    ans = merge(left, right)
    print(ans)
"""
3
EWPGAJRB
BB
TPQJDRJWSQXGRRIPXFMINTELHBJA
"""
    