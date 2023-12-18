#
# FILE: angle_between_vector.py
# TASK: angle_between_vector
# LANG: PYTHON
# ID:   6610685247
#

import math

a_length, b_length, degrees = map(float, input().split())
c_length = 0

if 0 < a_length < 10**10 and 0 < b_length < 10**10 and 0 <= degrees < 180:
    c_length = math.sqrt(
        a_length**2
        + b_length**2
        - (2 * a_length * b_length * math.cos(math.radians(degrees)))
    )
    print(f"{c_length:.2f}")
else:
    print("INVALID")
