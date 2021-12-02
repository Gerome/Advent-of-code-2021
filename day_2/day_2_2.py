a=b=c=0
for d,e in[x.split()for x in open("a").read().splitlines()]:
    e=int(e)
    match d:
        case"forward":
            a+=e
            b+=c*e
        case"down":c+=e
        case"up":c-=e
print(b*a)