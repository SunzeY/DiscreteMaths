# -*- coding: utf-8 -*-
# @Time : 2021-04-14 23:06
# @Author : Ze Yi Sun
# @Site : BUAA
# @File : dataprocess.py
# @Software: PyCharm

with open("input.txt", 'r') as f:
    a = f.read()
    b = a.split("L")
    x = []
    y = []
    for item in b:
        if item != "":
            [xi, yi] = item.split(' ')[1:3]
            try:
                y.append(float(yi))
                x.append(float(xi))
            except:
                pass
    print(x)
    print(len(x))
    print(y)
    print(len(y))
with open("out.txt", "w") as fp:
    fp.write("[" + ", ".join([str(i) for i in x]) + "]")
    fp.write("\n\n\n")
    fp.write("[" + ", ".join([str(i) for i in y]) + "]")

