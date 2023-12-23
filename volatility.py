from random import randint
import sys, inspect

# , os

# white and a bunch of grays and then black
WHITE = 15
FADE_COLORS = [WHITE] + list(range(255, 231, -4)) + [0]


# 1 in X chance of a char spilling
SPILL_RARITY = 500


def colored(text, color):
    print(f"\x1b[38;5;{color}m{text}\x1b[0m")


# Example usage
fade_effect("Hello, Fading World!")


def roll_chance(chance: int) -> bool:
    return randint(1, chance) == 1


def spill_effect(input_string: str) -> str:
    lines = input_string.split("\n")
    width = max([len(x) for x in lines])
    lines = [x.ljust(width) for x in lines]

    # key: column, value: stuck character
    stuck = {}

    # stuck chars fade to black, so this calculates
    # how many rows ago the char was stuck
    def get_color(row: int) -> int:
        ago = len(lines) - stuck[column]

    res = []

    for line in lines:
        for ch in line:
            if ch.isspace():
                continue

            if roll_chance(SPILL_RARITY):
                stuck[line.index(ch)] = ch

        def process_char(col: int) -> str:
            current_ch = line[col]
            if not current_ch.isspace():
                return current_ch

            return stuck.get(col, current_ch)

        glitched_line = [process_char(col) for col in range(width)]
        res.append("".join(glitched_line))

    return "\n".join(res)


frame = inspect.currentframe() or sys.exit()
quine = inspect.getsource(frame)
quine = spill_effect(quine)
print(quine, end="")

# os.remove(__file__)
