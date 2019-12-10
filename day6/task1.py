with open("input.in", "r") as in_file:
    DATA = [x.split(")") for x in in_file.read().split("\n")]
orbits = {d[1]: d[0] for d in DATA}

direct = 0
indirect = 0
for obj, parent in orbits.items():
    direct += 1

    parent = orbits.get(parent, None)
    while parent is not None:
        indirect += 1
        parent = orbits.get(parent, None)

print(direct + indirect)
