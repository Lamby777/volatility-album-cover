from random import randint
import sys, inspect

# , os


# 1 in X chance of a char spilling
SPILL_RARITY = 20


def roll_chance(chance: int) -> bool:
    return randint(1, chance) == 1


def spill_effect(input_string: str) -> str:
    lines = input_string.split("\n")
    width = max([len(x) for x in lines])
    lines = [x.ljust(width) for x in lines]

    # key: column, value: stuck character
    stuck = {}

    res = []

    for line in lines:
        for ch in line:
            if ch.isspace():
                continue

            if roll_chance(SPILL_RARITY):
                stuck[line.index(ch)] = ch

        def process_char(col: int) -> str:
            return stuck.get(col, line[col])

        glitched_line = [process_char(col) for col in range(width)]
        res.append("".join(glitched_line))

    return "\n".join(res)


frame = inspect.currentframe() or sys.exit()
quine = inspect.getsource(frame)
quine = spill_effect(quine)
print(quine, end="")

# os.remove(__file__)
