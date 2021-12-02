total_horizontal = 0
total_depth = 0
aim = 0

for instr in open("data.txt").read().splitlines():
    instr, amount = instr.split()
    amount = int(amount)
    match instr:
        case "forward":
            total_horizontal += amount
            total_depth += aim * amount
        case "down":
            aim += amount
        case "up":
            aim -= amount

print(total_depth * total_horizontal)
