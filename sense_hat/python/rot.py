#!/usr/bin/python3

from sense_emu import SenseHat

import sys
import getopt
import json

sense = SenseHat()

roll = None
pitch = None
yaw = None

r_flag = False
p_flag = False
y_flag = False
unit = " "

scaler = 0.0174532925

sysarg = sys.argv[1:]

try:
    opts, args = getopt.getopt(sysarg, ':rpyu:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

for opt, arg in opts:
    if opt in '-r':
        r_flag = True
    if opt in '-p':
        p_flag = True
    if opt in '-y':
        y_flag = True
    if opt in '-u':
        unit = arg
        
orient = sense.get_orientation()

if unit != 'r' and unit != 'd': 
    print("Wrong unit!")
    
else:
    if r_flag:
       roll = round(orient["roll"],4)
       if unit == 'd':
            pass          #if chosen degrees don't scale
       elif unit == 'r':
            roll = roll*scaler
            
    if p_flag:
       pitch = round(orient["pitch"],4)
       if unit == 'd':
            pass
       elif unit == 'r':
            pitch = pitch*scaler
            
    if y_flag:
       yaw = round(orient["yaw"],4)
       if unit == 'd':
            pass
       elif unit == 'r':
            yaw = yaw*scaler
            
if r_flag or p_flag or y_flag:        
    json_exit = json.dumps({"Orientation":{"roll":roll,"pitch":pitch,"yaw":yaw}})
    print(json_exit)