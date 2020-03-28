#!/usr/bin/python3

from sense_emu import SenseHat

import sys
import getopt

x = -1
y = -1

sense = SenseHat()
sysarg = sys.argv[1:]

try:
    opts, args = getopt.getopt(sysarg, ':x:y:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

for opt, arg in opts:
    if opt in '-x':
        x = int(arg)
    if opt in '-y':
        y = int(arg)

if x < 0 or x > 7 or y < 0 or y > 7:
    print("Wrong coordinates!")
    exit(1)

else:
    sense.clear(0, 0, 0) #if wrong coordinates provided nothing will change
    sense.set_pixel(x, y, 255, 20, 147)
                

