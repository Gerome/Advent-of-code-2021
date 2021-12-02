a=b=0
for d,c in [x.split() for x in open("a").read().splitlines()]:
    c=int(c)
    match d:
        case "forward":a+=c
        case "down":b+=c
        case "up":b-=c
print(b*a)
