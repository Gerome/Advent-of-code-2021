from itertools import pairwise
print(len([int(y)-int(x)for(x,y)in pairwise(open("a").read().splitlines())if int(y)-int(x)>0]))