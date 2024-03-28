
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    l =[0] * 10
    for j in range(n, m+1):
        s = str(j)
        l[0] += s.count('0')
        l[1] += s.count('1')        
        l[2] += s.count('2')
        l[3] += s.count('3')
        l[4] += s.count('4')
        l[5] += s.count('5')
        l[6] += s.count('6')
        l[7] += s.count('7')
        l[8] += s.count('8')
        l[9] += s.count('9')
    print(*l)
"""
3
1 9
10 456
123 2437
"""