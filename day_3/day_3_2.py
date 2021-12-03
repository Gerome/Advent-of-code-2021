#should be 2545, 231, 587895
def x(m):
    d=open("a").read().split("\n")
    for i in range(12):
        n=list(zip(*d))
        d[:]=[val for val in d if val[i]==(m)[sum([int(value) for value in n[i]])>=len(d)/2]]
        if len(d)==1:
            return int(d[0],2)
print(x("01")*x("10"))
