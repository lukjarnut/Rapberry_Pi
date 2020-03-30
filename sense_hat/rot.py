#!/usr/bin/python3

from sense_emu import SenseHat

import sys
import getopt
import json

sense = SenseHat()

r_flag = 0
p_flag = 0
y_flag = 0
unit = " "

roll = None
pitch = None
yaw = None

sysarg = sys.argv[1:]

try:
    opts, args = getopt.getopt(sysarg, ':rpyu:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

for opt, arg in opts:
    if opt in '-r':
        r_flag = 1
    if opt in '-p':
        p_flag = 1
    if opt in '-y':
        y_flag = 1
    if opt in '-u':
        unit = arg
        
orient = sense.get_orientation()

if unit != 'r' and unit != 'd': 
    print("Wrong unit!")
    
else:
    if r_flag:
       roll = orient["roll"]
       if unit == 'd':
            pass
       elif unit == 'r':
            roll = roll*0.0174532925
            
    if p_flag:
       pitch = orient["pitch"]
       if unit == 'd':
            pass
       elif unit == 'r':
            pitch = pitch*0.0174532925
            
    if y_flag:
       yaw = orient["yaw"]
       if unit == 'd':
            pass
       elif unit == 'r':
            yaw = yaw*0.0174532925
            
if r_flag or p_flag or y_flag:        
    json_exit = json.dumps({"Orientation":{"roll":roll,"pitch":pitch,"yaw":yaw}})
    print(json_exit)