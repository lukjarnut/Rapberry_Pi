#!/usr/bin/python3

from sense_emu import SenseHat
from getch import getch
from time import sleep
import threading
import json

sense = SenseHat()

char = None
x_pos = 0
y_pos = 0
button_p = 0
#bool_1 = True #Program status on/off

def read():
    while True:
          global x_pos
          global y_pos
          global button_p
          for event in sense.stick.get_events():
              if event.action == "pressed":
                if event.direction == "up":
                    y_pos += 1
                    #print("y", y_pos)
                if event.direction == "down":
                    y_pos -= 1
                    #print("y", y_pos)
                if event.direction == "left":
                    x_pos -= 1
                    #print("x", x_pos)
                if event.direction == "right":
                    x_pos += 1
                    #print("x", x_pos)
                if event.direction == "middle":
                    button_p += 1
          sleep(0.5)
def write():
    while True:
       global x_pos
       global y_pos
       global button_p
       json_exit = json.dumps([{'x':x_pos},{'y':y_pos},{'b':button_p}])
       print(json_exit)
       sleep(1)

reader = threading.Thread(target=read)
writer = threading.Thread(target=write)

reader.start()
writer.start()