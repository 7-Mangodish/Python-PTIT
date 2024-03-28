
def rev(n):
    re= 0
    while n>0:
        re= re*10 + n%10
        n //=10
    return re

def sol(n):
    i=0
    while i<1000 and n%7 !=0:
        n += rev(n)
        i+=1
    if n %7 ==0 and i<=1000:
        return n
    return -1
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n= int(input())
        print(sol(n))
        
