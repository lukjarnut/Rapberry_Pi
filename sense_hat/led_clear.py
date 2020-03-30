#!/usr/bin/python3

from sense_emu import SenseHat

import sys

sense = SenseHat()

for x in range(8):
    for y in range(8):
        sense.set_pixel(x, y, 0, 0, 0)
                
