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

def ExpandNodeBFS(fringe, node):
    # this is the tricky bit

    # CASE 1: one chicken in boat
    # check which side boat is on
    if (node.data[2] == 1):
        #boat is on left side
        tmp = node.data
        if (tmp[0] >= 1):
            # check that there are chickens to move
            tmp[0] -= 1
            tmp[3] += 1
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 0
                tmp[5] = 1
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)
    else:
        #boat is on right side
        tmp = node.data
        if (tmp[3] >= 1):
            # check that there are chickens to move
            tmp[3] -= 1
            tmp[0] += 1
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 1
                tmp[5] = 0
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)

    # CASE 2: two chickens in boat
    # check which side boat is on
    if (node.data[2] == 1):
        #boat is on left side
        tmp = node.data
        if (tmp[0] >= 2):
            # check that there are chickens to move
            tmp[0] -= 2
            tmp[3] += 2
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 0
                tmp[5] = 1
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)
    else:
        #boat is on right side
        tmp = node.data
        if (tmp[3] >= 2):
            # check that there are chickens to move
            tmp[3] -= 1
            tmp[0] += 1
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 1
                tmp[5] = 0
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)

    # CASE 3: one wolf in boat
    # check which side boat is on
    if (node.data[2] == 1):
        #boat is on left side
        tmp = node.data
        if (tmp[1] >= 1):
            # check that there are wolves to move
            tmp[1] -= 1
            tmp[4] += 1
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 0
                tmp[5] = 1
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)
    else:
        #boat is on right side
        tmp = node.data
        if (tmp[4] >= 1):
            # check that there are wolves to move
            tmp[4] -= 1
            tmp[1] += 1
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 1
                tmp[5] = 0
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)

    # CASE 4: one wolf one chicken
    # check which side boat is on
    if (node.data[2] == 1):
        #boat is on left side
        tmp = node.data
        if (tmp[0] >= 1 and tmp[1] >= 1):
            # check that there are wolves and chickens to move
            tmp[0] -= 1
            tmp[3] += 1
            tmp[1] -= 1
            tmp[4] += 1
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 0
                tmp[5] = 1
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)
    else:
        #boat is on right side
        tmp = node.data
        if (tmp[3] >= 1 and tmp[4] >= 1):
            # check that there are wolves and chickens to move
            tmp[4] -= 1
            tmp[1] += 1
            tmp[3] -= 1
            tmp[0] += 1
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 1
                tmp[5] = 0
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)

    # CASE 5: two wolves in boat
    # check which side boat is on
    if (node.data[2] == 1):
        #boat is on left side
        tmp = node.data
        if (tmp[1] >= 2):
            # check that there are wolves to move
            tmp[1] -= 2
            tmp[4] += 2
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 0
                tmp[5] = 1
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)
    else:
        #boat is on right side
        tmp = node.data
        if (tmp[4] >= 2):
            # check that there are wolves to move
            tmp[4] -= 2
            tmp[1] += 2
            # check wolf condition
            if tmp[0] > tmp[1] and tmp[3] > tmp[4]:
                # all good, create node
                # switch boat
                tmp[2] = 1
                tmp[5] = 0
                # create node and add to bottom of fringe
                new_node = Node(tmp, node, None)
                heapq.heappush(fringe, new_node)
                # add new node to current node's children
                node.AddChildren(new_node)

# let's do some searching - based off of pseudocode from lecture slides
def GraphSearch(initial_data, goal_data, nc):
    # initialize closed as hash table (dict))
    closed = []

    # initialize fringe as priority queue using heapq
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, Node(initial_data, None, None))

    #let's go searching friendos
    searching = True
    result = 0

    while searching:
        # if we run out of options without finding solution
        if len(fringe) == 0:
            searching = False

        # pop off top node to play with
        target_node = heapq.heappop(fringe)

        if target_node.data == goal_data:
            result = target_node
            searching = False

        # TODO: Make sure this actually does the equality right
        elif target_node not in closed:
            closed.append(target_node)
            ExpandNodeBFS(fringe, target_node)

    return result

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
