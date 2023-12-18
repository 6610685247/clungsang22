#
# FILE: dot_on_line.py
# TASK: dot_on_line
# LANG: PYTHON
# ID:   6610685247
#

xa, ya, xb, yb, x, y = input().split()

xa = float(xa)
ya = float(ya)
xb = float(xb)
yb = float(yb)
x = float(x)
y = float(y)

if (
    -100 <= xa <= 100
    and -100 <= ya <= 100
    and -100 <= xb <= 100
    and -100 <= yb <= 100
    and -100 <= x <= 100
    and -100 <= y <= 100
):  # check input range
    if xb - xa != 0:  # check m at 90 degrees or not
        m = (yb - ya) / (xb - xa)  # find m
        if y == m * (x - xa) + ya:
            if (
                abs(x) <= abs(xa)
                and abs(x) <= abs(xb)
                and abs(y) <= abs(ya)
                and abs(y) <= abs(yb)
            ):  # check input(x,y) is not out of the line
                print("YES")
            else:
                print("NO")
    else:
        if xa == x and xb == x :
            if ya < y < yb or yb < y < ya:  # check input y is not out of the line
                print("YES")
            else:
                print("NO")
        else :
            print("NO")
else:
    print("INVALID")
