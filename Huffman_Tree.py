# -*- coding: utf-8 -*-
# @Time : 2021-04-07 23:49
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : Huffman_Tree.py
# @Software: PyCharm
import math


def Huffman_Tree(lis):
    tre = lis
    while len(tre) != 1:
        w = tre[0][0] + tre[1][0]
        w = math.floor(w*10000)/10000
        tre = [[w, tre[0], tre[1]]] + tre[2:]
        tre = sorted(tre, key=lambda x: x[0])
    return tre[0]


def huffmanCoding(subtree, code):
    if len(subtree) == 2:
        return [[subtree[1], code]]
    else:
        node0 = subtree[1]
        node1 = subtree[2]
        code = huffmanCoding(node0, code+'1') + huffmanCoding(node1, code+'0')
        return code


def huffmanCode(tree):
    code0 = huffmanCoding(tree[1], "1")
    code1 = huffmanCoding(tree[2], "0")
    return code0 + code1


if __name__ == "__main__":
    a = []
    c = input()
    while c != "":
        b = c.split(" ")
        a.append([float(b[1]), b[0]])
        c = input()
    a.sort()
    tree = Huffman_Tree(a)
    code = huffmanCode(tree)
    for item in code:
        print(item)
