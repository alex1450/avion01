#!/usr/bin/env python3

"""
    AVu 2020.04.04 Test running python on mac
"""

import matplotlib.pyplot as plt

foil_x = []
foil_y = []

filename = "0012.txt"

foil = open(filename, "r")


for line in foil:
    value = line.split()
    # print(value)
    foil_x.append(float(value[0]) * 200.0)
    foil_y.append(float(value[1]) * 200.0)

# print(foil_x)
plt.plot(foil_x, foil_y)
plt.xlim(-10, 210)
plt.ylim(-110, 110)
plt.show()
