# should be 354129
import statistics
data=[int(x)for x in open("b").read().split(",")]
print(int(sum([abs(d-statistics.mean(data))for d in data])))