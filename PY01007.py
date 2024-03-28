from math import *


if __name__== '__main__':
     t= int(input())
     while t>0:
        str =input().split()
        n, x, m =map(float, str)
        ans =log(m/n, 1+x/100)
        ans=ceil(ans)
        print(ans)
        t-=1
        
          
          