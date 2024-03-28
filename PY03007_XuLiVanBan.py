import re

l =''
while True:
    try:
        l+=(input().lower())
    except EOFError:
        break

ar=[]
pattern ='[\.\?\!]'
ar = re.split(pattern, l)
# print(ar)
ar.remove('')
for i in ar:
    w = i.split()
    w[0]=w[0].capitalize()
    print(*w)

"""
ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
"""