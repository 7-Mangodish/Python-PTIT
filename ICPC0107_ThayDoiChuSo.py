
if __name__=='__main__':
    t =int(input())
    while t>0:
        a, b= map(str, input().split())
        s1= input().strip()
        if s1.count(' ')!=0:
            s1, s2= map(str, s1.split())
        else:
            s2= input()
        minVal= min(a, b)
        maxVal= max(a, b)
        print(int(s1.replace(maxVal, minVal)) + int(s2.replace(maxVal, minVal)), end=' ')
        print(int(s1.replace(minVal, maxVal)) + int(s2.replace(minVal, maxVal)), end='\n')
        t-=1
"""
1
5 6
645
666
TestCase đặc biệt: x1 chứa dấu cách, 2 số cùng nằm trên một dòng
"""
