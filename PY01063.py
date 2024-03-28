from math import*

def sol(s1, s2):
    cnt=0
    ind =0
    while ind<len(s1):
        if s1[ind : ind+len(s2)] == s2:
            cnt+=1
            ind+=len(s2)
        else:
            ind+=1
    return cnt

if __name__ == '__main__':
    t =int(input())
    while t>0:
        s1= input()
        s2= input()
        print(sol(s1,s2))
        t-=1