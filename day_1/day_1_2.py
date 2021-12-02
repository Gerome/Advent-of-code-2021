a=[];i=b=0
for d in open("a").read().splitlines():
    a.append(int(d))
    if len(a)>3:
        del a[0]
        c=sum(a)
        if c>b:i+=1
        b=c
print(i)