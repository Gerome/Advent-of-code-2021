# Should be 355386
days = range(80)
eights = 0
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

# current = [2,3,2,0,1]
for day in days:
    eights = data[0]
    zeros = data[0]
    # current = [6 if x-1 == -1 else x-1 for x in current]
    for i in range(9):
        data[i] = data[i+1]
    data[8] += eights
    data[6] += eights
print(sum(data.values()))

