#!/usr/bin/env python

# driver for aiSearch 
# run using: search.py initial_state_file goal_state_file mode output_file
# by Michaela Buchanan

import sys
import os

initial_file = sys.argv[1]
goal_file = sys.argv[2]
mode = sys.argv[3]
output_file = sys.argv[4]

if(mode == "bfs"):
    cmd = "algorithms/bfs.py " + sys.argv[1] + sys.argv[2]+ sys.argv[3]+ sys.argv[4]
    os.system(cmd)

elif mode == "dfs":
    cmd = "algorithms/dfs.py " + sys.argv[1] + sys.argv[2]+ sys.argv[3]+ sys.argv[4]
    os.system(cmd)

elif(mode == "iddfs"):
    cmd = "algorithms/iddfs.py " + sys.argv[1] + sys.argv[2]+ sys.argv[3]+ sys.argv[4]
    os.system(cmd)

elif(mode == "astar"):
    cmd = "algorithms/astar.py " + sys.argv[1] + sys.argv[2]+ sys.argv[3]+ sys.argv[4]
    os.system(cmd)

else:
    print("The command you entered was not recognized. Please use the following format: search.py initial_state_file goal_state_file mode output_file")

