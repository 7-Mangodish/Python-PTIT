from math import*

if __name__ == '__main__':
    s= list(input())
    s.reverse()
    sum=0
    ans=[]
    for i in range(len(s)):
        ind= i%3
        if ind==0:
            ans.append(sum)
            sum=0
        sum+= (int(s[i])*(2**ind))
    if sum !=0:
        ans.append(sum)
    ans.reverse()
    ans.pop()
    for i in ans:
        print(i, sep='', end='')

