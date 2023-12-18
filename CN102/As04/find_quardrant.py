#
# FILE: find_quardrant.py
# TASK: find_quardrant
# LANG: PYTHON
# ID:   6610685247
#

x, y = input().split()

x = float(x)
y = float(y)

if (
    abs(x) >= 10**20 or abs(y) >= 10**20 or x == 0 or y == 0
):  # check that input value is in range or not
    print("Error")
else:
    if x > 0 and y > 0:  # (+,+)
        print("I")
    elif x < 0 and y > 0:  # (-,+)
        print("II")
    elif x < 0 and y < 0:  # (-,-)
        print("III")
    else:  # (+,-)
        print("IV")
