
t = int(input())
for i in range(t):
    s = input()
    st = []
    ans = []
    ind = 1
    for j in s:
        if j =='(':
            st.append(ind)
            ans.append(ind)
            ind +=1
        elif j == ')':
            top = st.pop()
            ans.append(top)
    print(*ans)

"""
2
(a + (b *c) ) + (d/e)
( ( () ) ( () ) )
"""