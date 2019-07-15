e=int(input())
a=[]
for i in range(e):
    v=input()
    a.append(v)
n=len(a)
c=[]
for i in range(0,n):
    c.append(len(a[i]))
s=min(c)
b=[]
for k in range(0,n): 
    for i in a[k]:
        if(k<n-1):
            for j in a[k+1]:
                    if(i==j):
                        b.append(i)
b = list(dict.fromkeys(b))
for i in b:
    print(i,end="")
    
            
