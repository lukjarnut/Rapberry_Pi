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

def observer(): #function waiting for char and stopping read and write
    try:
        None
    except BaseException:
       reader.join()
       writer.join()
       sys.exit(0)
    
def read():
    while True:
        try:
          global stop
          global x_pos
          global y_pos
          global button_c
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
          
          sleep(0.5)
        except (KeyboardInterrupt, SystemExit):
            reader.join()
            writer.join()
            sys.exit(0)
def write():
    while True:
       global stop
       global x_pos
       global y_pos
       global button_c
       json_exit = json.dumps([{'x':x_pos},{'y':y_pos},{'b':button_c}])
       fil = open('joy_data.dat', 'a')
       fil.write(json_exit)
       fil.write(',')
       print(json_exit)
       sleep(1)
        
reader = threading.Thread(target=read)
writer = threading.Thread(target=write)

fil = open('joy_data.dat', 'w')
fil.write('[')
fil.write(']')

reader.start()
writer.start()


# char = getch.getch()
# if char != None:
#   status = True
#   break