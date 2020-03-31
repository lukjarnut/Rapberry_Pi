#!/usr/bin/python3

from sense_emu import SenseHat
import getch
from time import sleep
import threading
import json

sense = SenseHat()

x_pos = 0
y_pos = 0
button_c = 0
 
try: 
    while True:
        for event in sense.stick.get_events(): #get events from sensehat joystick
            if event.action == "pressed": #getting direction
                if event.direction == "up": #handling direction
                    y_pos += 1
                if event.direction == "down":
                    y_pos -= 1
                if event.direction == "left":
                    x_pos -= 1
                if event.direction == "right":
                    x_pos += 1
                if event.direction == "middle":
                    button_c += 1
                
        sleep(1)
        json_exit = json.dumps({"Joystick":{"x":x_pos,"y":y_pos,"button":button_c}}) #creating json
        fil = open('joy_data.dat', 'w')
        fil.write(json_exit)
        print(json_exit)   
except (KeyboardInterrupt, SystemExit): #keyboard interrupt (Ctrl+C)
    exit()
