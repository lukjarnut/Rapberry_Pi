#!/usr/bin/python3

import sys
import getopt

period=0

sysarg = sys.argv[1:]

try:
    opts, args = getopt.getopt(sysarg, 'rw:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

try:
    for opt, arg in opts:
        if opt in '-r':
            fil = open('led_blink_period.dat', 'r')
            print(fil.read())
        if opt in '-w':
            temp = arg
            fil = open('led_blink_period.dat', 'w')
            fil.seek(0)
            fil.write(temp)
            print("Saved new value: ",temp)
        fil.close()   
except IOError:
    print("Cannot open file")
    sys.exit(1)
  
