with open(__file__.replace(".py", ".in"), "r") as in_file:
    DATA = [x.split(")") for x in in_file.read().split("\n")]
orbits = {d[1]: d[0] for d in DATA}


def get_chain(obj):
    chain = []
    while obj is not None:
        chain.append(obj)
        obj = orbits.get(obj, None)
    return chain


you_chain = get_chain(orbits["YOU"])
santa_chain = get_chain(orbits["SAN"])

for i in range(1, min(len(you_chain), len(santa_chain)) + 1):
    if you_chain[-i:] != santa_chain[-i:]:
        shared = i - 1

        # number of transfers
        print(len(you_chain) + len(santa_chain) - 2 * shared)
        # the path
        print(you_chain[:-shared] + santa_chain[:-shared + 1][::-1])

        break
