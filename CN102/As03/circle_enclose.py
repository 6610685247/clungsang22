#
# FILE: circle_enclose.py
# TASK: circle_enclose
# LANG: PYTHON
# ID:   6610685247
#

import math

cx, cy, r, x, y = input().split()

cx = float(cx)
cy = float(cy)
r = float(r)
x = float(x)
y = float(y)

d = math.sqrt(
    ((x - cx) ** 2) + ((y - cy) ** 2)
)  # d is distance between center of the circle and the input(x,y)

if d <= r:
    print("1")  # input(x,y) position is in circle or on the circle outline
else:
    print("0")  # input(x,y) position is out of circle
