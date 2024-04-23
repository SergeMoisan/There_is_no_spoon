# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:22:39 2023

@author: serge

There is no spoon
"""
board = ("0.0.0.")
nodes = []
h = 3
w = 3

k = 0

line_0 = (".00")
line = list(line_0)

for j in range(w):
    if line[j] == '0':
        nodes.append([j, k])
k += 1


for i in range(len(nodes)):
    print('x1 = ', nodes[i][0], 'y1 = ', nodes[i][1])

for node in nodes:
    right_neighbourg = [[u, v] for [u, v] in nodes if u !=
                        w and v == node[1] and (u != node[0])]
    print(node, ' right_neighbourg = ', right_neighbourg)


def right_neighbourg(node, nodes):
    x = node[0]
    y = node[1]
    for x_p in range(x+1, w+1):
        if [x_p, y] in nodes:
            voisin_droite = [x_p, y]
            return(voisin_droite)
    return [-1, -1]


def lower_neighbourg(node, nodes):
    x = node[0]
    y = node[1]
    for y_p in range(y+1, h+1):
        if [x, y_p] in nodes:
            voisin_dessous = [x, y_p]
            return(voisin_dessous)
    return [-1, -1]


for node in nodes:
    voisin_droite = right_neighbourg(node, nodes)
    voisin_dessous = lower_neighbourg(node, nodes)
    print(node[0], '', node[1], '', voisin_droite[0], '',
          voisin_droite[1], '', voisin_dessous[0], '', voisin_dessous[1])
