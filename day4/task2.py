import re
import collections

with open(__file__.replace(".py", ".in"), "r") as in_file:
    MIN, MAX = (int(x.strip()) for x in in_file.read().split("-"))

passwords = [i for i in range(MIN, MAX + 1)
             if re.search(r"(.)\1", str(i))  # duplicated adjacent
             and 2 in collections.Counter(str(i)).values()  # 2 of one number
             and re.search(r"^0*1*2*3*4*5*6*7*8*9*$", str(i))]  # increasing
print(len(passwords))
