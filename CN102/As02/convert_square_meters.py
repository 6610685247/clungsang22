#
# FILE: convert_square_meters.py
# TASK: convert_square_meters
# LANG: PYTHON
# ID:   6610685247
#

x, y = input().split()

x = int(x)

if x >= 10000000 or x <= 0:
    print("Error")

if y == "1":
    rai = x / 1600
    print("%.2f" % rai)

if y == "2":
    ngan = x / 400

    print("%.2f" % ngan)

if y == "3":
    square_wa = x / 4
    print("%.2f" % square_wa)
