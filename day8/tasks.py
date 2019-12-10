with open("input.in", "r") as in_file:
    data = in_file.read().strip()

width = 25
height = 6
size = width * height

layers = [data[i:i + size] for i in range(0, len(data), size)]

# task 1

layer = min(layers, key=lambda l: l.count("0"))
print("Task 1 =", layer.count("1") * layer.count("2"))

# task 2

print("\nTask 2 =")

image = []
for i in range(size):
    for layer in layers:
        if layer[i] in ("0", "1"):
            image.append(layer[i])
            break
    else:
        raise ValueError

for y in range(height):
    for x in range(width):
        print("■" if int(image.pop(0)) else " ", end="")
    print()
