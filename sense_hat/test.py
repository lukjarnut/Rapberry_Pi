#!/usr/bin/python3

#script checking if multithreading works

import threading
import time

value = 0
def read_value(): #thread for reading value
    while True:
        global value
        time.sleep(3)
        print("Read value is: " + str(value))
def increment_value():
    while True:
        global value
        time.sleep(3)
        print("Value before incrementing: " + str(value))
        value +=1

incr_thread = threading.Thread(target=increment_value)
read_thread = threading.Thread(target=read_value)
incr_thread.start()
read_thread.start()

