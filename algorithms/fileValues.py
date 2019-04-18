#!/usr/bin/env python

# input from initial file
def GetVals(data, file):
    in_file_name = "data/" + file 
    file = open(in_file_name)

    left_line = file.readline()

    data[0] = left_line.split(',')[0]
    data[1] = left_line.split(',')[1]
    data[2] = left_line.split(',')[2]

    right_line = file.readline()

    data[3] = right_line.split(',')[0]
    data[4] = right_line.split(',')[1]
    data[5] = right_line.split(',')[2]