from random import randint;                        import sys, inspect, os ############
FADE_SPD = 1; SPILL_RARITY                                 = 10; ':)'; WHITE = 15 ####
FG_COLOR = 9;  FADE_COLORS                                     = [WHITE] + list( ####
range(255, 231, -FADE_SPD)                                 ); ''; to_exec =    ''"""
def colored(text__, colr):                               return f"\x1b"""'' + (####
'[38;5;{colr}m{text__}'''+                              '\x1b[0m" ########' ) ####
exec("#################\n"                             + to_exec+"\n######") ####
def roll_chance(chnc: int)                           -> bool:return randint(####
1, chnc) == 1 ############                          ###########################
to_exec = '##########\n' +                        "###############\n" + ( ####
"""def spill_effect(inputs                       :str) -> str: ##############
\tlines = inputs.split (((                      "\\n")))\n\twidth = max(####
[len(x) for x in lines]) ;                     lines = [x.ljust(width) ####
for x in lines] + [] + [];                    stuck={};\n\tdef getcol(####
row: int, col: int) ->int:                  \n\t\tstuck_s= stuck.get(####
                                          ##############################
###########################################///////////////////////########################################################################################
col)\n\t\tif stuck_s    is    None:      return WHITE;           ####          //////  //      //////  //////  //////  //      //////  //////  //  //  ##
\t\tago = row - stuck_s - 4       ;     return FADE_COLORS[min( ####          //  //  //      //  //    //      //    //        //      //    //////  ##
max(ago, 0), len(FADE_COLORS) -1)];   "an album by Cherry C."; ####          //  //  //      //////    //      //    //        //      //        //  ##
#######################################     OwO UwU :3 <3 :D  ####          //////  //////  //  //    //    //////  //////  //////    //    //////  ##
######################################///////////////////////########################################################################################
\tres = []                          ############################
\tfor lineno, line in ((((         enumerate(lines)  )))): ####
\t\tfor i,ch in enumerate(        line):\n\t\t\tif ch in [####
" ", "#", "/"]:   continue       \n\t\t\tif roll_chance( ####
SPILL_RARITY): stuck[i] = lineno
\t\tdef process_char(col: int) -> str:
\t\t\tcurrent_ch = line[col]
\t\t\tif not current_ch.isspace(): return colored(current_ch, FG_COLOR)
\t\t\tst = stuck.get(col)
\t\t\tch_to_print = lines[st][col] if st else current_ch
\t\t\treturn colored(ch_to_print, getcol(lineno, col))
\t\tglitched_line = [process_char(col) for col in range(width)]
\t\tres.append("".join(glitched_line))
\treturn "\\n".join(res)
""")
exec(to_exec)

frame = inspect.currentframe() or sys.exit()
quine = inspect.getsource(frame)
quine = spill_effect(quine)
print(quine, end="")
# os.remove(__file__)
