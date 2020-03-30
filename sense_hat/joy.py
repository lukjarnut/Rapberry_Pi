#!/usr/bin/python3

from sense_emu import SenseHat
import getch
from time import sleep
import threading
import json

sense = SenseHat()

char = None
x_pos = 0
y_pos = 0
button_c = 0
stop = False #Program status on/off
   
while True:
      for event in sense.stick.get_events():
          if event.action == "pressed":
            if event.direction == "up":
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
       json_exit = json.dumps([{'x':x_pos},{'y':y_pos},{'b':button_c}])
       fil = open('joy_data.dat', 'w')
       fil.write(json_exit)
       fil.write(',')
       print(json_exit)
