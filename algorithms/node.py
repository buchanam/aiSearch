#!/usr/bin/env python

class Node:
    'Class for node objects used for GraphSort'
    children = [None]

    def __init__(self, data, parent, children):
        self.__data = data
        self.__parent = parent
        self.__f_val = None
        if children != None:
            for child in children:
                self.children.append(child)

    def AddChild(self, child):
        self.children.append(child)

    @property
    def data(self):
        return self.__data

    @property
    def parent(self):
        return self.__parent

    @property
    def f_val(self):
        return self.__f_val

    def generate_fval(self, goal):
        x = len(self.__data)
        total = 0
        # heuristic total
        for y in range(0, x):
            total += abs(self.__data[y] - goal[y])
        # cost total
        parent_node = self.__parent
        while (parent_node != None):
            total += 1
            parent_node = parent_node.parent
        self.__f_val = total
