
def check(s):
    for i in range(0, len(s)-1, 1):
         if s[i] >s[i+1]:
              return False
    return True

if __name__=='__main__':
    t =int(input())
    while(t>0):
        str =input()
        if(check(str)):
              print('YES')
        else:
             print('NO')
        t-=1
         
