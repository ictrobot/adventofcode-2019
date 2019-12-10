with open(__file__.replace(".py", ".in"), "r") as in_file:
    data = in_file.read().strip()

width = 25
height = 6
size = width * height

layers = [data[i:i + size] for i in range(0, len(data), size)]

layer = min(layers, key=lambda l: l.count("0"))
print(layer.count("1") * layer.count("2"))