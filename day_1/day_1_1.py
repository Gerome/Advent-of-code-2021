t=[int(x)for x in open("a").read().split("\n")]
print(len([0for i,j in zip(t[:-1],t[1:]) if j-i>0]))