
def check(s):
    if s=='6' or s=='68' or s=='688':
        return True
    return False

s = input()
ind =0
while ind < len(s):
    if ind +3<=len(s) and check(s[ind: ind + 3]):
        ind +=3
    elif ind +2 <= len(s) and check(s[ind: ind+2]):
        ind +=2
    elif ind +1 <= len(s) and  check(s[ind:ind+1]):
        ind +=1
    else:
        break

if(ind == len(s)):
    print('YES')
else:
    print('NO') 
