#!/usr/bin/env python

class Node:
    'Class for node objects used for GraphSort'
    children = [None]

    def __init__(self, data, parent, children):
        self.__data = data
        print(self.__data)
        self.__parent = parent
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
