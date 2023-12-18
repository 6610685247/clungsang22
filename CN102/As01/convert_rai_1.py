#
# FILE: convert_rai_1.py
# TASK: convert_rai_1
# LANG: PYTHON
# ID:   6610685247
#

a, b, c = input().split()  # type a b c  #use 'whitespace'
a = int(a)
b = int(b)
c = int(c)
if 0 <= a <= 100000 and 0 <= b <= 100000 and 0 <= c <= 100000:
    area = (a * 1600) + (b * 400) + (c * 4)
    print(area)
else:
    print("Error")
