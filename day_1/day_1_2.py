a=[]
i=b=0
for d in open("a").read().split("\n"):
    a.append(int(d))
    if len(a)>3:
        _,*a=a
        c=sum(a)
        if c>b:i+=1
        b=c
print(i)