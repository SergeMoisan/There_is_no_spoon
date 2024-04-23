# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:22:39 2023

@author: serge

There is no spoon
"""
board = ("0.0.0.")
nodes = []
h = 3
w = 2
line_0 = ("0.")
line_0[0]
for i in range(h):
    for j in range(w):
        if board[j+i] == '0':
            nodes = nodes + [[i, j]]

nodes[0]

for node in nodes:
    x1 = node[0]
    x2 = node[1]
    print(x1, '', x2)
