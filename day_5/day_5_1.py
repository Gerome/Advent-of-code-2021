# Should be 6005
data=[[eval(val) for val in coord.split(" -> ")] for line in open("a").read().split("\n") for coord in line.split(", ")]
board = [[0 for i in range(1000)] for i in range(1000)]

for start, end in data:
    diff = max(abs(end[0] - start[0]), abs(end[1]-start[1]))

    def set_step(index):
        if start[index] < end[index]: return 1
        elif start[index] == end[index]: return 0
        else : return -1

    step_x = set_step(0)
    step_y = set_step(1)

    if step_x == 0 or step_y == 0:
        for i in range(diff+1):
            board[start[1] + i * step_y][start[0] + i * step_x] += 1

print(sum([1 for row in board for val in row if val >=2]))
