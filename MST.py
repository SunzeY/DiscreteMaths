# -*- coding: utf-8 -*-
# @Time : 2021-04-17 22:47
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : MST.py
# @Software: PyCharm

import graph.graph as gp


def Kruskal(V, E):
    base = list(range(0, len(V)))
    dic = dict(map(lambda x, y: [x, y], V, base))
    E_cache = sorted(E, key=lambda x: x[2])
    mstEdges = []
    while E_cache:
        u, v, d = E_cache.pop(0)
        if dic[u] != dic[v]:
            mstEdges.append((u, v, d))
            for key, value in dic.items():
                if value == dic[v]:
                    dic[key] = dic[u]
    return mstEdges


def Prim(V, E):
    vNum = len(V)
    E = sorted(E, key=lambda x: x[2])
    v_mst = [E[0][0]]
    E_mst = []
    E_cache = [E[0]]
    for edge in E:
        if (edge[0] == E[0][0] or edge[1] == E[0][0]) and edge not in E_cache:
            E_cache.append(edge)
    count = 0
    while count < vNum - 1 and E_cache:
        u, v, w = E_cache.pop(0)
        if u in v_mst and v in v_mst:
            continue
        E_mst.append((u, v, w))
        if u not in v_mst:
            v_mst.append(u)
            addV = u
        else:
            v_mst.append(v)
            addV = v
        count += 1
        for vi, w, d in E:
            if vi == addV and w not in v_mst:
                E_cache.append((vi, w, d))
            if w == addV and vi not in v_mst:
                E_cache.append((vi, w, d))
        E_cache.sort(key=lambda x: x[2])
    return E_mst


if __name__ == "__main__":
    V = ['a', 'b', 'c', 'd', 'e', 'f']
    E = [('a', 'b', 1), ('b', 'c', 2), ('c', 'd', 3), ('d', 'a', 4),
         ('a', 'e', 5), ('a', 'f', 8), ('c', 'f', 7), ('c', 'e', 6),
         ('b', 'f', 9), ('e', 'd', 10)]
    gp.drawweightgraph(E)
    E_mst1 = Kruskal(V, E)
    E_mst2 = Prim(V, E)
    gp.drawweightgraph(E_mst1)
    gp.drawweightgraph(E_mst2)
