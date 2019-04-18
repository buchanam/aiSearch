#!/usr/bin/env python

class Node:
    'Class for node objects used for GraphSort'
    parent = None
    children = []
    data = [None] * 6

    def __init__(self, data, parent, children):
        self.data = data
        self.parent = parent
        for child in children:
            self.children.append(child)

    def AddChild(self, child):
        self.children.append(child)
