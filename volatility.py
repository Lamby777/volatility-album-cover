import sys, inspect, random

# , os

# chance of a row
SPILL_CHANCE = 100


def spill(input_string: str):
    lines = input_string.split("\n")
    width = max([len(x) for x in lines])
    lines = [x.ljust(width) for x in lines]

    # index = column, value = row to copy (or None if not stuck)
    stuck_rows = [None for x in range(width)]

    res = []

    for line in lines:
        glitched_line = [stuck_rows[ch] or line[ch] for ch in range(width)]
        res.append("".join(glitched_line))

    return "\n".join(res)


frame = inspect.currentframe() or sys.exit()
quine = inspect.getsource(frame)
quine = spill(quine)
print(quine, end="")

# os.remove(__file__)
