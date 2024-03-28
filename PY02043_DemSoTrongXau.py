

def sol(s1, s2):
    ind =0; k= len(s2)
    ans=0
    while ind <= len(s1)-k:
        tmp= s1[ind : ind +k]
        # print(tmp)
        # ind += k
        if tmp == s2:
            ans+=1
            ind = ind+k
        else:
            ind+=1
    return ans

t= int(input())
for _ in range(t):
    s1= input()
    s2= input()
    # sol(s1, s2)
    ans= sol(s1, s2)
    print(ans)
"""
2
1212121112211221121
121
2222222222322292
2222
"""