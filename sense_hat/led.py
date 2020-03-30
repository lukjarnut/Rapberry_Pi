#!/usr/bin/python

import sys
import getopt
from sense_emu import SenseHat

sense = SenseHat()

x = -1
y = -1
red = 0
green = 0
blue = 0

sysarg = sys.argv[1:];

try:
    opts,args = getopt.getopt(sysarg, ':x:y:r:g:b:')
except getopt.GetoptError as err:
            print(err)
            sys.exit(1)
            
for opt, arg in opts:
    if opt in '-x':
        x = int(arg)
    if opt in '-y':
        y = int(arg)
    if opt in '-r':
        red = int(arg)
    if opt in '-g':
        green = int(arg)
    if opt in '-b':
        blue = int(arg)
        
if x < 0 or x > 7 or y < 0 or y > 7:
    print("Wrong coordinates!")
    exit(1)
    
else:         
    if red == 0 or green == 0 or blue == 0:
        print("Nie wybrano koloru")
        sense.clear(0, 0, 0) #if wrong coordinates provided nothing will change
        exit(1)
    else:
        sense.set_pixel(x, y, red, green, blue)