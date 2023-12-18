#
# FILE: average_1.py
# TASK: average_1
# LANG: PYTHON
# ID:   6610685247
#

input_num = input().split()

n = int(input_num[0])
sum = 0

if n == 0 :
    print("0.000")
else :
    for count in range(1, n + 1):
        x = float(input_num[count])
        if 0 <= x <= (10**10) :
            sum += x

    average = sum / n
    print(f"{average:.3f}")
