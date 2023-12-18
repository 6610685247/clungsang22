#
# FILE: angle_between_vector.py
# TASK: angle_between_vector
# LANG: PYTHON
# ID:   6610685247
#

import math

x1, y1, x2, y2 = map(float, input().split())

theta_rad = 0
theta_deg = 0

u_vector = math.sqrt(x1**2 + y1**2)
v_vector = math.sqrt(x2**2 + y2**2)

if u_vector == 0 or v_vector == 0:
    print("INVALID")
else:
    theta_rad = math.acos((x1 * x2 + y1 * y2) / (u_vector * v_vector))

    theta_deg = math.degrees(theta_rad)

    print(f"{theta_deg:.2f}")
