# Should be 8442
d=open("a").read().split("\n\n")
n,f=[int(v)for v in d[0].split(",")],[[[int(v)for v in r.split()] for r in b.splitlines()] for b in d[1:]]
z=enumerate
r=range
c=[[]for _ in r(len(f))]
s=sum
for m in n:
    for i,b in z(f):
        p=[(x,y)for x,li in z(b)for y,val in z(li)if val==m]
        if p:
            c[i].append(p[0])
            t=list(zip(*c[i]))
            w=[1 for e in t for h in r(5)if e.count(h)==5]
            if w:
                raise Exception(m*(s(s(b,[]))-s(b[x][y]for x,y in c[i])))
