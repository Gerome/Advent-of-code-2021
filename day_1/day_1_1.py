t=[int(x)for x in open("a").read().splitlines()]
print(len([0for i,j in zip(t[:-1],t[1:]) if j-i>0]))