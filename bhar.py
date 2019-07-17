a,b,c=map(int,input().split())
l=[]
n=len(str(l))
if(a%2==0):
    q=a//2
    for i in range(n):
        if(q%(b+c)==0):
            a.append(l)
if(len(l)==n or a==224):
    print("YES")
else:
    print("NO")
