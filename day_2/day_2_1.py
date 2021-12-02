total_horizontal = 0
total_depth = 0

for instr in open("data.txt").read().splitlines():
    instr, amount = instr.split()
    amount = int(amount)
    match instr:
        case "forward":
            total_horizontal += amount
        case "down":
            total_depth += amount
        case "up":
            total_depth -= amount

print(total_depth * total_horizontal)
