#!/usr/bin/env python3

"""
    AVu 2020.04.04 Test running python on mac
"""

import matplotlib.pyplot as plt

wing_x = []
wing_y = []
emp_x = []
emp_y = []

filename_wing = "clarky.txt"
filename_emp = "0012.txt"

foil = open(filename_wing, "r")
emp = open(filename_emp, "r")

for line in emp:
    value = line.split()
    emp_x.append(float(value[0]) * 100.0)
    emp_y.append(float(value[1]) * 100.0)

for line in foil:
    value = line.split()
    wing_x.append(float(value[0]) * 200.0)
    wing_y.append(float(value[1]) * 200.0)

plt.plot(wing_x, wing_y, emp_x, emp_y)
# plt.plot(emp_x, emp_y)
plt.xlim(-10, 210)
plt.ylim(-110, 110)
plt.show()
