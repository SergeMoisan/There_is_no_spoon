# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 19:15:28 2023

@author: serge
"""

import sys
#import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
nodes = []
k = 0
for i in range(height):
    line = input()  # width characters, each either 0 or .
    liste = list(line)
    for j in range(width):
        if line[j] == '0':
            nodes.append([j, k])
    k += 1


def right_neighbour(node, nodes):
    x = node[0]
    y = node[1]
    for x_p in range(x+1, width+1):
        if [x_p, y] in nodes:
            voisin_droite = [x_p, y]
            return(voisin_droite)
    return [-1, -1]


def lower_neighbour(node, nodes):
    x = node[0]
    y = node[1]
    for y_p in range(y+1, height+1):
        if [x, y_p] in nodes:
            voisin_dessous = [x, y_p]
            return(voisin_dessous)
    return [-1, -1]


for node in nodes:
    voisin_droite = right_neighbour(node, nodes)
    voisin_dessous = lower_neighbour(node, nodes)
    print(node[0], '', node[1], '', voisin_droite[0], '',
          voisin_droite[1], '', voisin_dessous[0], '', voisin_dessous[1])

# Write an action using print

#print("1 0 -1 -1 0 0")
print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor
#print("0 0 1 0 0 1")
