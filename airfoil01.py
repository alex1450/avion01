#!/usr/bin/env python3

"""
    AVu 2020.04.13 Airfoil calculation
"""

import matplotlib.pyplot as plt

# array for coefficient
wing_alpha_coef = []    # angle of attack
wing_cl_coef = []       # lift coefficient
wing_cd_coef = []       # drag coefficient
wing_cm_coef = []       # pitch moment coefficient
emp_alpha_coef = []    # angle of attack
emp_cl_coef = []       # lift coefficient
emp_cd_coef = []       # drag coefficient
emp_cm_coef = []       # pitch moment coefficient

# array to plot profile
wing_x_profile = []
wing_y_profile = []
emp_x_profile = []
emp_y_profile = []

wing_lenght = 460.0
wing_chord = 200.0
wing_thickness = 11.7 * wing_chord / 100.0
emp_chord = 100.0
emp_shift = 300.0

velocity = 5    # m/s
wing_angle = 5
emp_angle = 0

file_wing_profile = "clarky.txt"
file_emp_profile = "0012.txt"

file_wing_coef = "clarky_coef.txt"
file_emp_coef = "0012_coef.txt"


# mass calculation in gramms
# chassis
balsa_flange = 5    # 2x per plane
queue = 5           # 5 x 10 x 500mm queue
extruded_core = 0

chassis_mass = 2 * balsa_flange + queue + extruded_core

# wings
wing_mass = 0.66*wing_thickness / 1000.0 * wing_lenght / 1000.0 * \
    wing_chord / 1000.0 * 35.0 * 1000.0
emp_mass = 0.0

# electro
battery_mass = 30.0
feather_mass = 5.5
motor_mass = 5.0          # 2x motor
servo_mass = 10.0

electro_mass = battery_mass + feather_mass + 2 * motor_mass

# total mass
total_mass = chassis_mass + electro_mass

# plot coeficient
wing_coef = open(file_wing_coef, "r")
emp_coef = open(file_emp_coef, "r")

i = 0
for line in wing_coef:
    if i > 2:
        value = line.split()
        wing_alpha_coef.append(float(value[0]))
        wing_cl_coef.append(float(value[1]))
        wing_cd_coef.append(float(value[2]))
        wing_cm_coef.append(float(value[3]))
    i += 1

i = 0
for line in emp_coef:
    if i > 2:
        value = line.split()
        emp_alpha_coef.append(float(value[0]))
        emp_cl_coef.append(float(value[1]))
        emp_cd_coef.append(float(value[2]))
        emp_cm_coef.append(float(value[3]))
    i += 1

fig, ((wing_cl, wing_cd), (wing_cm, profile)) = plt.subplots(2, 2)
fig.suptitle('Main wing coefficient')
wing_cl.plot(wing_alpha_coef, wing_cl_coef)
wing_cd.plot(wing_alpha_coef, wing_cd_coef)
wing_cm.plot(wing_alpha_coef, wing_cm_coef)

# plot airfoil shape
wing_profile = open(file_wing_profile, "r")
emp_profile = open(file_emp_profile, "r")

for line in wing_profile:
    value = line.split()
    wing_x_profile.append(float(value[0]) * wing_chord)
    wing_y_profile.append(float(value[1]) * wing_chord)

for line in emp_profile:
    value = line.split()
    emp_x_profile.append(float(value[0]) * emp_chord + emp_shift)
    emp_y_profile.append(float(value[1]) * emp_chord)

# calculating lift drag and pitch moment


profile.plot(wing_x_profile, wing_y_profile, emp_x_profile, emp_y_profile)
# profile.xlim(-10, 210 + emp_shift - 100.0)
# profile.ylim(-110, 110)
# plt.show()
