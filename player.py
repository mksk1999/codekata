a,b=map(str,input().split())
for i in range(len(a)):
    if(a.count(a[i])==b.count(b[i])):
        print("yes")
        break
    else:
        print("no")
        break
