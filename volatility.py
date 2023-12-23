import sys, inspect, random

# , os


def spill(input_string: str):
    lines = input_string.split("\n")
    width = max([len(x) for x in lines])
    lines = [x.ljust(width) for x in lines]

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
