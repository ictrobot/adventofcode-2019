lines = []
with open("input.in", "r") as in_file:
    for l in in_file:
        lines.append([x.strip() for x in l.split(",")])

DIRECTIONS = {
    "U": lambda x, y: (x, y + 1),
    "D": lambda x, y: (x, y - 1),
    "L": lambda x, y: (x - 1, y),
    "R": lambda x, y: (x + 1, y)
}


def get_points(line):
    point = (0, 0)
    points = []

    for command in line:
        dir = command[0]
        length = int(command[1:])
        for i in range(1, length + 1):
            point = DIRECTIONS[dir](*point)
            points.append(point)

    return set(points)


def manhattan_distance(p):
    return abs(p[0]) + abs(p[1])


line1, line2 = lines
points1 = get_points(line1)
points2 = get_points(line2)

intersection = []
for p1 in points1:
    if p1 in points2:
        intersection.append(p1)

intersection.sort(key=lambda p: (manhattan_distance(p), p))

print(manhattan_distance(intersection[0]))