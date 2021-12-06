# Should be 355386
import time

start = time.time()

days = range(256)
current = [int(x) for x in open("a").read().split(",")]

data = {
    0: current.count(0),
    1: current.count(1),
    2: current.count(2),
    3: current.count(3),
    4: current.count(4),
    5: current.count(5),
    6: current.count(6),
    7: current.count(7),
    8: current.count(8),
    9: 0
}

for day in days:
    eights = data[0]
    for i in range(9):
        data[i] = data[i+1]
    data[8] += eights
    data[6] += eights
print(sum(data.values()))

end = time.time()
print(end - start)