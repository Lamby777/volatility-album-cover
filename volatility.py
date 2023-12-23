import sys, inspect, random

# , os

# chance of a row
SPILL_CHANCE = 100


def spill(input_string: str):
    lines = input_string.split("\n")
    width = max([len(x) for x in lines])
    lines = [x.ljust(width) for x in lines]

    # key: column, value: stuck character
    stuck = {}

    res = []

    for line in lines:
        glitched_line = [stuck.get(col, line[col]) for col in range(width)]
        res.append("".join(glitched_line))

    return "\n".join(res)


frame = inspect.currentframe() or sys.exit()
quine = inspect.getsource(frame)
quine = spill(quine)
print(quine, end="")

# os.remove(__file__)
