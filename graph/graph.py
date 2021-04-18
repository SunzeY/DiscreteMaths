# -*- coding: utf-8 -*-
# @Time : 2021-03-29 22:39
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : graph.py
# @Software: PyCharm

import networkx as nx
import matplotlib.pyplot as plt


def drawgraph(E):
    G = nx.Graph()
    G.add_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return


def drawDiGraph(E):
    G = nx.DiGraph()
    G.add_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return


def drawweightgraph(E):
    G = nx.Graph()
    G.add_weighted_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return



def adjacentList(V, E):
    Ea = []
    for w in V:
        e0 = [w]
        e1 = []
        for (u, v) in E:
            if u == w and v not in e1:
                e1.append(v)
            if v == w and u not in e1:
                e1.append(u)
        e0 += [sorted(e1)]
        Ea += [e0]
    return sorted(Ea)


# Hamilton cycle algorithm
def tourPath0(V, E, path, m):
    while len(path) < m:
        w = path[-1]
        i = V.index(w)
        Ea = E[i][1]
        for u in Ea:
            if u not in path:
                path.append(u)
                break
        if path[-1] == w:
            break
    return path


def tourPath1(V, E, path):
    u = path.pop()
    while len(path) != 0:
        v = path[-1]
        Ea = E[V.index(v)][1]
        k = Ea.index(u)
        while k < len(Ea) - 1:
            k += 1
            u = Ea[k]
            if u not in path:
                path.append(u)
                break
        if path[-1] != v:
            break
        u = path.pop()
    return path


def tourPath(V, E, path, m):
    if len(path) == m:
        path = tourPath1(V, E, path)
    while len(path) != 0:
        path = tourPath0(V, E, path, m)
        if len(path) == m:
            break
        path = tourPath1(V, E, path)
    return path


def HamiltonPath(V, E, v0):
    V = sorted(V)
    Ea = adjacentList(V, E)
    paths = set({})
    path = [v0]
    m = len(V)
    path = tourPath(V, Ea, path, m)
    paths = paths | {tuple(path)}
    while len(path) == m:
        path = tourPath(V, Ea, path, m)
        if len(path) == m:
            paths = paths | {tuple(path)}
    return paths

