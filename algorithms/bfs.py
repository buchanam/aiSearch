#!/usr/bin/env python

# bfs for aiSearch 
# run using: bfs.py initial_state_file goal_state_file mode output_file
# by Michaela Buchanan

import sys
import os
import heapq
from node import Node
from fileValues import GetVals

# assign cmd line args to variables
initial_file = sys.argv[1]
goal_file = sys.argv[2]
mode = sys.argv[3]
output_file = sys.argv[4]



# let's do some searching - based off of pseudocode from lecture slides
def GraphSearch(initial_data, goal_data, nc):
    # initialize closed as hash table (dict))
    closed = {}

    # initialize fringe as priority queue using heapq
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, Node(initial_data, None, None))

    return 0



#######################################  Main ##############################################

# get data from input into list of form lC, lW, lB, rC, rW, rB
initial_data = [None] * 6
goal_data = [None] * 6

GetVals(initial_data, initial_file)
GetVals(goal_data, goal_file)

# run bf graph search on data
node_counter = 0
result = GraphSearch(initial_data, goal_data, node_counter)

# display result 
if result == 0:
    print("No solution was found :(")
