a=b=0
for d,c in[x.split() for x in open("a").read().split("\n")]:
    c=int(c)
    match d[0]:
        case"f":a+=c
        case"d":b+=c
        case"u":b-=c
print(b*a)
