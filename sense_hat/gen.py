#!/usr/bin/python3

file = open('temp.dat', 'w')

for i in range(8):
    for j in range(8):
        if j == 7:
            tem = "<br>"
        else:
            tem = ""
        file.write("<input type=\"checkbox\" name=\"%d%d\" value=\"1\"> %s \n" % (i, j, tem))