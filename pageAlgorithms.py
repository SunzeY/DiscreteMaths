# -*- coding: utf-8 -*-
# @Time : 2021-04-16 9:43
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : pageAlgorithms.py
# @Software: PyCharm

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Opt(pages):
    missCnt = [0] * 11
    for n in range(1, 11):
        cache = []
        m = 0
        while len(cache) < n:
            if pages[m] not in cache:
                cache.append(pages[m])
                missCnt[n] += 1
            m += 1
        k = m
        if n == 2:
            k = m
        while k < len(pages):
            if pages[k] not in cache:
                future = [1000] * n
                for u in range(0, n):
                    for t in range(k+1, len(pages)):
                        if pages[t] == cache[u]:
                            future[u] = t - n
                            break
                maxi = 0
                maxIndex = 0
                for v in range(0, n):
                    if future[v] > maxi:
                        maxIndex = v
                        maxi = future[v]
                cache[maxIndex] = pages[k]
                missCnt[n] += 1
            k += 1
    return missCnt[1:]


def Fifo(pages):
    missCnt = [0] * 11
    for n in range(1, 11):
        cache = []
        m = 0
        while len(cache) < n:
            if pages[m] not in cache:
                cache.append(pages[m])
                missCnt[n] += 1
            m += 1
        k = m
        while k < len(pages):
            if pages[k] not in cache:
                cache.pop()
                cache.append(pages[k])
                missCnt[n] += 1
            k += 1
    return missCnt[1:]


def LRU(pages):
    missCnt = [0] * 11
    for n in range(1, 11):
        cache = []
        m = 0
        while len(cache) < n:
            if pages[m] not in cache:
                cache.append(pages[m])
                missCnt[n] += 1
            m += 1
        k = m
        while k < len(pages):
            if pages[k] in cache:
                index = 0
                for i in range(0, len(cache)):
                    if cache[i] == pages[k]:
                        index = i
                        break
                cache[-1], cache[index] = cache[index], cache[-1]
            else:
                cache.pop()
                cache.append(pages[k])
                missCnt[n] += 1
            k += 1
    return missCnt[1:]

def show_axis():
    plt.xlim(0, 11)
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    plt.ylim(0, 100)
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    for i in range(10):
        plt.plot([0, 11], [(i+1)*10, (i+1)*10], linewidth='1', color='aliceblue')
        plt.plot([i+1, i+1], [0, 100],  linewidth='1', color='aliceblue', )


def show_graph(opt_faults, lru_faults, fifo_faults):
    show_axis()
    ln1, = plt.plot(x, opt_faults, color='blueviolet', marker='o', markersize='3')
    ln2, = plt.plot(x, lru_faults, color='green', marker='^', markersize='3')
    ln3, = plt.plot(x, fifo_faults, color='gold', marker='D', markersize='3')
    plt.legend([ln1, ln2, ln3], ['OPT', 'LRU', 'FIFO'])
    for i in range(10):
        plt.text(i + 1, opt_faults[i] + 1, str(opt_faults[i]), ha='center', va='bottom', fontsize='8')
        plt.text(i + 1, lru_faults[i] + 1, str(lru_faults[i]), ha='center', va='bottom', fontsize='8')
        plt.text(i + 1, fifo_faults[i] + 1, str(fifo_faults[i]), ha='center', va='bottom', fontsize='8')
    plt.show()


if __name__ == "__main__":
    pages = [0, 9, 8, 4, 4, 3, 6, 5, 1, 5, 0, 2, 1, 1, 1, 1, 8, 8, 5, 3,
             9, 8, 9, 9, 6, 1, 8, 4, 6, 4, 3, 7, 1, 3, 2, 9, 8, 6, 2, 9,
             2, 7, 2, 7, 8, 4, 2, 3, 0, 1, 9, 4, 7, 1, 5, 9, 1, 7, 3, 4,
             3, 7, 1, 0, 3, 5, 9, 9, 4, 9, 6, 1, 7, 5, 9, 4, 9, 7, 3, 6,
             7, 7, 4, 5, 3, 5, 3, 1, 5, 6, 1, 1, 9, 6, 6, 4, 0, 9, 4, 3]
    OptMiss = Opt(pages)
    LRUMiss = LRU(pages)
    FifoMiss = Fifo(pages)
    capacity = range(1, 10+1)
    show_graph(OptMiss, LRUMiss, FifoMiss)
    print(OptMiss)
    print(LRUMiss)
    print(FifoMiss)
    print('Done.')

