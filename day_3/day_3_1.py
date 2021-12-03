# Answer should be 4001724
z=open("a").read().split("\n")
x="".join(["1"if sum([int(bit) for bit in i])>len(z)/2 else"0"for i in zip(*z)])
print(int(x,2)*int(''.join("01"[i<"1"]for i in x),2))
