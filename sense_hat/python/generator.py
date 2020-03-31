#!/usr/bin/python3

file = open('gen_output.dat', 'w')

for i in range(8):
    for j in range(8):
        if j == 7:
            tem = "<br>"
        else:
            tem = ""
        file.write("<input type=\"text\" name=\"%d%d\" size=\"1\"> %s \n" % (j, i, tem))