fuel = 0

with open("input.in", "r") as in_file:
    values = [int(line) // 3 - 2 for line in in_file.readlines()]

while values:
    fuel += sum(x for x in values if x > 0)
    values = [x // 3 - 2 for x in values if x > 0]

print(fuel)
