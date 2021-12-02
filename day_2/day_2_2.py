a=b=c=0
for d,e in[x.split()for x in open("a").read().splitlines()]:
    e=int(e)
    match d[0]:
        case"f":
            a+=e
            b+=c*e
        case"d":c+=e
        case"u":c-=e
print(b*a)