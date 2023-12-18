#
# FILE: convert_rai_2.py
# TASK: convert_rai_2
# LANG: PYTHON
# ID:   6610685247
#

x = int(input())

if 0 < x < 10000000:
    rai = x // 1600
    ngan = (x % 1600) // 400
    square_wa = (x % 400) / 4.0

    print(rai, ngan, "%.2f" % (square_wa))
else:
    print("Error")
