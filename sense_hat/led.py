#!/usr/bin/python

import sys
import getopt
from sense_emu import SenseHat

sense = SenseHat()

x = -1
y = -1
color = ''

sysarg = sys.argv[1:];

try:
    opts,args = getopt.getopt(sysarg, ':x:y:c:')
except getopt.GetoptError as err:
            print(err)
            sys.exit(1)
            
for opt, arg in opts:
    if opt in '-x':
        x = int(arg)
    if opt in '-y':
        y = int(arg)
    if opt in '-c':
        color = arg
        
if x < 0 or x > 7 or y < 0 or y > 7:
    print("Wrong coordinates!")
    exit(1)

elif (color == 'R') or (color == 'r'):
    sense.set_pixel(x, y, 255, 0, 0)  #setting color to red
elif (color == 'G') or (color == 'g'):
    sense.set_pixel(x, y, 0, 255, 0)
elif (color == 'B') or (color == 'b'):
    sense.set_pixel(x, y, 0, 0, 255)
else:
    print("No color chosen!")
    sense.clear(0, 0, 0)