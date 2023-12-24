from random import randint;"12/23/2023";       import sys, inspect, os ####################
FADE_SPD = 1; SPILL_RARITY                             = 10; ':)'; WHITE = 15 ############
FG_COLOR = 9;  FADE_COLORS                                 = [WHITE] + list( ############
range(255, 231, -FADE_SPD)                             ); ''; to_exec =    ''"""
def colord(text,    colr):                           return f"\x1b"""'' + (####
'[38;5;{colr}m{text}'  ''+                          '\x1b[0m" ########' ) ####
exec("#################\n"                         + to_exec+"\n######") ####         2037
def roll_chance(chnc: int)                       -> bool:return randint(####                   I... don't even know...
1, chnc) == 1 ############                      ###########################
to_exec = '##########\n' +                    "###############\n" + ( ####
"""def spill_effect(inputs                   :str) -> str: ##############
\tlines = inputs.split (((                  "\\n")))\n\twidth = max(####
[len(x) for x in lines]) ;                 lines = [x.ljust(width) ####
for x in lines] + [] + [];                stuck={};\n\tdef getcol(####
row: int, col: int) ->int:              \n\t\tstuck_s= stuck.get(####
                                       #############################
###########################################///////////////////////####################################################################################
col)\n\t\tif stuck_s    is    None: ' '; return WHITE;           ##        //////  //      //////  //////  //////  //      //////  //////  //  //  ##
\t\tago = row - stuck_s - 4       ;' '; return FADE_COLORS[min( ##        //  //  //      //  //    //      //    //        //      //    //////  ##
max(ago, 0), len(FADE_COLORS) -1)];"'; AN ALBUM BY CHERRY C."; ##        //  //  //      //////    //      //    //        //      //        //  ##
#######################################     OwO UwU :3 <3 :D  ##        //////  //////  //  //    //    //////  //////  //////    //    //////  ##
                                 #####///////////////////////####################################################################################
\tres = []                                               ####
\tfor lineno, line in ((((      enumerate(lines)  )))): ####
\t\tfor i,ch in enumerate(     line):\n\t\t\tif ch in [####                    ####     #####
" ", "#", "/"]:   continue    \n\t\t\tif roll_chance( ####                   #######  ########
SPILL_RARITY): stuck[i]  =   lineno\n\t\tdef process(####                   //////////////////###################
col: int) ->          str:  \n\t\t\tcur_ch=line[col]####                   ##################
\t\t\tif       not cur_ch. isspace():return colord(####                     ###############
cur_ch, FG_COLOR)         \n\t\t\tst = stuck.get( ####           ############/////////////
col )\n\t\t\tch_to_print =( lines[st][col] if st ####                          ########
else cur_ch)\n\t\t\treturn colord( ch_to_print, ####                             ####
getcol(lineno, col))   \n\t\tglitched_line = [ ####
process(col) for col in range(width)] ############
\t\tres.append("".join(glitched_line)) ##########
\treturn "\\n".join(res)""");exec(to_exec)  ####
frame=inspect.currentframe() or sys.exit() ####
quine=inspect.getsource(frame) ###############
quine=spill_effect(quine);print(quine,end="")
os.remove(__file__) ## Leave it alone... ###
###########################################





