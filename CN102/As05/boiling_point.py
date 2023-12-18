#
# FILE: boiling_point.py
# TASK: boiling_point
# LANG: PYTHON
# ID:   6610685247
#

bp = float(input())

if 0.0 <= bp <= 10**4:
    if (100 * 95 / 100) <= bp <= (100 * 105 / 100):  # check water boiling point +-5%
        print("water")
    elif (
        (357 * 95 / 100) <= bp <= (357 * 105 / 100)
    ):  # check mercury boiling point +-5%
        print("mercury")
    elif (
        (1187 * 95 / 100) <= bp <= (1187 * 105 / 100)
    ):  # check copper boiling point +-5%
        print("copper")
    elif (
        (2193 * 95 / 100) <= bp <= (2193 * 105 / 100)
    ):  # check silver boiling point +-5%
        print("silver")
    elif (2660 * 95 / 100) <= bp <= (2660 * 105 / 100):  # check gold boiling point +-5%
        print("gold")
    else:
        print("unknown")  # input boiling point is not specified in the list
else:
    print("invalid")  # input boiling point is not in input boiling point range
