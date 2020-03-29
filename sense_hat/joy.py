#!/usr/bin/python3

from sense_emu import SenseHat
from getch import getch
from time import sleep

sense = SenseHat()

char = None
x_pos = 0
y_pos = 0
button_p = 0

while True:
      for event in sense.stick.get_events():
          if event.action == "pressed":
            if event.direction == "up":
                y_pos += 1
                print("y_pos: ",y_pos)
            if event.direction == "down":
                y_pos -= 1
                print("y_pos: ", y_pos)
            if event.direction == "left":
                x_pos -= 1
                print("x_pos: ", x_pos)
            if event.direction == "right":
                x_pos += 1
                print("x_pos: ", x_pos)
            if event.direction == "middle":
                button_p += 1
                print("Pressed ", button_p, "times")
                
       #char = getch()
       #if char != None:
       #     break