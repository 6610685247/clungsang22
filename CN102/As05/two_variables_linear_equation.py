#
# FILE: two_variables_linear_equation.py
# TASK: two_variables_linear_equation
# LANG: PYTHON
# ID:   6610685247
#

a, b, c = input().split()  # ax + by +c = 0

a = float(a)
b = float(b)
c = float(c)

if -10 <= a <= 10 and -10 <= b <= 10 and -10 <= c <= 10:
    if a == 0 and b == 0:
        print("-2")  # a and b are 0
    elif b == 0:
        print("2")  # m are infinity (b is 0)
    elif -a / b > 0:
        print("1")  # m is positive (angle is less than 90 degrees)
    elif -a / b == 0:
        print("0")  # m is 0 and b is not 0 (angle is 90 degrees)
    else:
        print("3")  # m is negative (angle is more than 90 degrees)
else:
    print("-1")  # input value is out of input range
