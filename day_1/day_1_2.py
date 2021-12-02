a = []
i = 0
prev = 0
for depth in open("a").read().splitlines():
    a.append(int(depth))
    if len(a)>3:
        del a[0]
    if len(a)==3:
        curr=sum(a)
        if curr>prev:
            i+=1
        prev=curr
print(i)