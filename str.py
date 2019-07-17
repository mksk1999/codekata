a=list(map(str,input().split()))
e=a[0]
f=a[1]
b=len(a[0])
c=len(a[1])
s=min(b,c) 
if(b>c):
    g=e[s:]
if(b<c):
    g=f[s:]
print(g)
d=0
if(b>c):
    for i in range(len(g)):
        d+=ord(g[i])-96
elif(c>b):
    for i in range(len(g)):
        d+=ord(g[i])-96
else:
    d=0
for i in range(s):
    if(a[0][i]!=a[1][i]):
        d+=abs(ord(a[0][i])-ord(a[1][i]))
print(d)

