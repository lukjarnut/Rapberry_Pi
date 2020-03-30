#!/usr/bin/python3

from sense_emu import SenseHat

import sys
import getopt
import json

sense = SenseHat()

h_flag=0
p_flag=0
t_flag=0

h_unit=" "
p_unit=" "
t_unit=" "

humidity = None
pressure = None
temperature = None

sysarg = sys.argv[1:]

try:
    opts, args = getopt.getopt(sysarg, ':h:p:t:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

for opt, arg in opts:
    if opt in '-h':
        h_flag = 1
        h_unit = arg
    if opt in '-p':
        p_flag = 1
        p_unit = arg
    if opt in '-t':
        t_flag = 1
        t_unit = arg
        
if h_flag:
    humidity = sense.get_humidity()
    if h_unit == "%":
        pass
    elif h_unit == "d":
        humidity = humidity/100
    else:
        print('-h wrong unit')
        sys.exit(1)
if p_flag:
   pressure = sense.get_pressure()
   if p_unit == "hpa":
        pass 
   elif p_unit == "mmhg":
        pressure = 0.75006 * pressure
   else:
        print('-p wrong unit')
        sys.exit(1)
if t_flag:
    temperature = sense.get_temperature()
    if ( t_unit == 'C' or t_unit == 'c' ):
        pass
    elif t_unit == 'F' or t_unit == 'f':
        temperature = 32+1.8*float(temperature)
    else:
        print('-t wrong unit')
        sys.exit(1)
        
if h_flag or p_flag or t_flag:        
    json_exit = json.dumps([{"humi":humidity},{"press":pressure},{"temp":temperature}])
    print(json_exit)