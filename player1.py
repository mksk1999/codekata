a=input()
b=len(a)
c=[]
for i in range (0,b,2):
    c.append(a[i:i+2][::-1]) 
print("".join(c))
        
