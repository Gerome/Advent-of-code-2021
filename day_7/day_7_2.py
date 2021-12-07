# should be 98905973
import math
import statistics
f=[int(x)for x in open("a").read().split(",")]
print(int(sum([sum(range(abs(i-math.floor(statistics.mean(f)))+1)) for i in f])))