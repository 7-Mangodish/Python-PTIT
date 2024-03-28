
a=[]
gr=[]
t= int(input())
for _ in range(t):
    s= input()
    if s!='':
        gr.append(s)
    else:
        tmp= [x for x in gr]
        a.append(tmp)
        gr.clear()
if len(gr)!=0:
    a.append(gr)
for i in range(len(a)):
    print(a[i][0], ':', sep='', end=' ')
    print(len(a[i])-1)
"""
9
Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?

Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?
"""