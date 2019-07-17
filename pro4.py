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
for i in range(len(g)):
    d+=ord(g[i])-96
print(d)
for i in range(s):
    d+=abs(ord(e[i])-ord(f[i]))
print(d)

