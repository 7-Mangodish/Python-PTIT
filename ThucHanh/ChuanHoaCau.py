import re

s = ""
regex = '[\w\s,:]+'
while True: 
    try : s += input()
    except EOFError : break
s = re.findall(regex, s)
for i in s:
    x = i.lower().split()
    x[0] = x[0].title()
    print(' '.join(x))
"""
Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
moi    CAC BAN danG ky     thaM giA !
"""