from random import randint; import sys, inspect, os
FADE_SPEED = 1; SPILL_RARITY = 10; WHITE = 15; CODE_COLOR = 14
FADE_COLORS = [WHITE] + list(range(255, 231, -FADE_SPEED))
def colored(text, color): return f"\x1b[38;5;{color}m{text}\x1b[0m"
def roll_chance(chance: int) -> bool: return randint(1, chance) == 1
def spill_effect(input_string: str) -> str:
    lines = input_string.split("\n")
    width = max([len(x) for x in lines])
    lines = [x.ljust(width) for x in lines]
    stuck = {}
    def get_color(row: int, col: int) -> int:
        stuck_start = stuck.get(col)
        if stuck_start is None: return WHITE
        ago = row - stuck_start
        return FADE_COLORS[min(ago, len(FADE_COLORS) - 1)]
    res = []
    for lineno, line in enumerate(lines):
        for i, ch in enumerate(line):
            if ch.isspace(): continue
            if roll_chance(SPILL_RARITY): stuck[i] = lineno
        def process_char(col: int) -> str:
            current_ch = line[col]
            if not current_ch.isspace(): return colored(current_ch, CODE_COLOR)
            st = stuck.get(col)
            ch_to_print = lines[st][col] if st else current_ch
            return colored(ch_to_print, get_color(lineno, col))
        glitched_line = [process_char(col) for col in range(width)]
        res.append("".join(glitched_line))
    return "\n".join(res)
frame = inspect.currentframe() or sys.exit()
quine = inspect.getsource(frame)
quine = spill_effect(quine)
print(quine, end="")
os.remove(__file__)
