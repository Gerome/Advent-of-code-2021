#should be 2545, 231, 587895
def x(m):
    d=open("a").read().split("\n")
    for i in range(12):
        d[:]=[v for v in d if v[i]==(m)[sum([int(x) for x in list(zip(*d))[i]])>=len(d)/2]]
        if len(d)==1:
            return int(d[0],2)
print(x("01")*x("10"))
