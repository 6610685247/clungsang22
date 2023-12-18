#
# FILE: square_enclose.py
# TASK: square_enclose
# LANG: PYTHON
# ID:   6610685247
#

tlx, tly, brx, bry, x, y = input().split()

tlx = float(tlx)
tly = float(tly)
brx = float(brx)
bry = float(bry)
x = float(x)
y = float(y)

if tlx == brx or tly == bry:
    print("-1")  # can't create rectangle
elif tlx <= x <= brx and tly <= x <= bry:
    print("1")
else:  # input out of rectangle
    print("0")
