from  math import*

def sol(s):
    for i in s:
        if i.isdigit()== False:
            s= s.replace(i,' ')
    l= [int(x) for x in s.split()]
    print(min(l))
if __name__=='__main__':
    t= int(input())
    while t>0:
        s= input()
        sol(s)
        t-=1

"""
2
12ab29cd19
ab123gh456cd
"""