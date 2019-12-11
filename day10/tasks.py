import math
import collections

asteroids = []
with open("input.in", "r") as in_file:
    for y, line in enumerate(in_file.read().strip().splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                asteroids.append((x, y))


def visible(loc):
    seen = set()
    x, y = loc

    for (x2, y2) in asteroids:
        delta = (x2 - x, y2 - y)
        gcd = math.gcd(*delta)
        direction = tuple(d / (gcd if gcd > 0 else 1) for d in delta)

        if direction not in seen:
            seen.add(direction)

    seen.remove((0, 0))
    return len(seen)


def laser(loc):
    angles = {}
    distances = collections.defaultdict(list)
    x, y = loc

    for (x2, y2) in asteroids:
        delta = (x2 - x, y2 - y)
        gcd = math.gcd(*delta)
        direction = tuple(d / (gcd if gcd > 0 else 1) for d in delta)
        distance = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
        distances[direction].append((distance, (x2, y2)))

        angles[direction] = math.atan2(delta[0], -delta[1]) % (math.pi * 2)

    del angles[0, 0]
    del distances[0, 0]

    for direction, _ in sorted(angles.items(), key=lambda x: x[1]):
        distances[direction].sort(key=lambda x: x[0])

    output = []
    while len(output) < len(asteroids) - 1:
        for direction, _ in sorted(angles.items(), key=lambda x: x[1]):
            if distances[direction]:
                output.append(distances[direction].pop(0)[1])
    return output


# task 1
best = max(asteroids, key=visible)
print("Task 1:", best, visible(best))

# task 2
order = laser(best)
vaporized200 = order[199]
print("Task 2:", vaporized200, vaporized200[0] * 100 + vaporized200[1])