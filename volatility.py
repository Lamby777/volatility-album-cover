import sys, inspect, os


#    _   ______  __   ___ ____________   ____________  __
#   | | / / __ \/ /  / _ /_  __/  _/ /  /  _/_  __/\ \/ /
#   | |/ / /_/ / /__/ __ |/ / _/ // /___/ /  / /    \  /
#   |___/\____/____/_/ |_/_/ /___/____/___/ /_/     /_/
#


frame = inspect.currentframe() or sys.exit()
quine = inspect.getsource(frame)
print(quine, end="")

os.remove(__file__)
