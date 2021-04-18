# -*- coding: utf-8 -*-
# @Time : 2021-04-01 17:34
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : Dijkstra.py
# @Software: PyCharm

def degreesetw(V, E):
    V = sorted(V)
    m = len(V)
    di = [0] * m
    do = [0] * m
    d = [0] * m
    for (w, u, v) in E:
        i = V.index(u)
        j = V.index(v)
        di[j] += 1
        do[i] += 1
        d[i] += 1
        d[j] += 1
    return [d, di, do]


def shortpath(V, E, di, Hx, path, zn):
    V = sorted(V)
    Pm = []
    for p in path:
        vn = p[-1]
        if vn == zn:
            Pm = Pm + [p]
            continue
        if di[V.index(vn)] != 0:
            Pm = Pm + [p]
            continue
        for (w, u, v) in E:
            if u == vn:
                kv = V.index(v)
                if di[kv] > 0:
                    di[kv] = di[kv]-1
                vw = p[0]+w
                if vw <= Hx[kv]:
                    Hx[kv] = vw
                    e = [vw] + p[1:] +[v]
                    Pm = Pm +[e]
    return [di, Hx, Pm]


def shortestpath(V, E, v0, vn):
    V = sorted(V)
    [d, di, do] = degreesetw(V, E)
    Pm0 = []
    Pm = [[0, v0]]
    inf = 10000
    Hx = [inf for x in range(len(V))]
    Hx[0] = 0
    while Pm0 != Pm:
        Pm0 = Pm
        [di, Hx, Pm] = shortpath(V, E, di, Hx, Pm0, vn)
    Pm = sorted(Pm)
    return [Hx, Pm]


if __name__ == "__main__":
    V = ['a', 'b', 'c', 'd', 'e', 'z']
    E = {(4, 'a', 'b'), (2, 'a', 'd'), (3, 'b', 'c'), (3, 'b', 'e'),
         (2, 'c', 'z'), (3, 'd', 'e'), (1, 'e', 'z')}
    [Hx, Pm] = shortestpath(V, E, V[0], V[-1])
    print(V)
    print(E)
    print(Hx, Pm)
