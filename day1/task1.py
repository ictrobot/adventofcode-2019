with open(__file__.replace(".py", ".in"), "r") as in_file:
    print(sum(int(line) // 3 - 2 for line in in_file.readlines()))
