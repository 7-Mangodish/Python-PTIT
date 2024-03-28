
import functools 

def cmp (o1, o2):
    w1 = o1.name.split(' ')
    w2 = o2.name.split(' ')
    name1 = w1.pop()
    name2 = w2.pop()

    sur1 = ''
    for i in w1:
        sur1 += i +' '
    sur2 = ''
    for i in w2:
        sur2 += i +' '

    if name1 < name2:
        return -1
    elif name1 == name2:
        return sur1 < sur2
    return 1

class In4:
    def __init__(self, name, num, time):
        self.name = name
        self.num = num
        w = time.split(' ')
        self.time = w[1]
    
    def out(self):
        print(f'%s: %s %s'%(self.name, self.num, self.time))

with open('E:\CODE\Python\File\SOTAY.txt') as f:
    lines = f.readlines()

l=[] #Luu index
a=[]
for i in range(len(lines)):
    if lines[i].startswith('Ngay'):
        l.append(i)
l.append(len(lines))
# print(l)

for i in range(len(l)-1):
    ind =1
    tmp =[]
    while l[i] + ind < l[i+1]:
        name = lines[l[i] + ind].rstrip()
        num = lines[l[i] + ind +1].rstrip()
        ind +=2
        # print(name, num)
        tmp.append(In4(name, num, lines[l[i]].rstrip()))
    tmp.sort(key = functools.cmp_to_key(cmp) )
    a.extend(tmp)
for i in a:
    i.out()
# with open('DIENTHOAI.txt', 'r') as f2:
#     for i in a:


