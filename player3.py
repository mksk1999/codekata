l,r=map(int,input().split())
b=0
for i in range(l,r+1):
    c=1
    for j in range(l,r+1):
        if(i%j==0):
            c+=1
    if(c==2):
        b+=1
print(b)
    
    





