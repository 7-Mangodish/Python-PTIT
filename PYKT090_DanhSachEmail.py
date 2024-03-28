
with open('CONTACT.in') as f:
    lines = f.readlines()
s = set()
for i in lines:
    s.add(i.strip().lower())
s = sorted(s, key = lambda x: x)
for i in s:
    print(i)