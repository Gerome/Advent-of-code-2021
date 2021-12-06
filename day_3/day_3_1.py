# Answer should be 4001724
g=int
z=open("a").read().split("\n")
x="".join(["10"[sum([g(y) for y in i])>len(z)/2]for i in zip(*z)])
print(g(x,2)*g(''.join("01"[i<"1"]for i in x),2))
