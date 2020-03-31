#!/usr/bin/python3

import sys
import getopt

t_flag=0
h_flag=0
p_flag=0
unit=" "

sysarg = sys.argv[1:]

try:
    opts, args = getopt.getopt(sysarg, ':hpt:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

for opt, arg in opts:
    if opt in '-h':
        h_flag = 1
    if opt in '-p':
        p_flag = 1
    if opt in '-t':
        unit = arg
        t_flag = 1
        
if h_flag:
    h_dat = open('/home/pi/Lab_01/temperature.dat', 'r')
    print(h_dat.read())
if p_flag:
    p_dat = open('/home/pi/Lab_01/pressure.dat', 'r')
    print(p_dat.read())
if t_flag:
    t_dat_C = open('/home/pi/Lab_01/temperature.dat', 'r')
    if(unit == 'c' or unit == 'C'):
        print(t_dat_C.read())
    elif(unit == 'f' or unit == 'F'):
        t_dat_F = 32+1.8*float(t_dat_C.read())
        print(t_dat_F)
    else:
        print('wrong unit')
        sys.exit(1)