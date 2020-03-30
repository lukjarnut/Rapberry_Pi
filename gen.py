#!/usr/bin/python3

file = open('temp.dat', 'w')

for i in range(8):
    for j in range(8):
        file.write("<input type=\"checkbox\" id=\"%d_%d\" name=\"%d.%d\"> \n" % (i, j, i, j))