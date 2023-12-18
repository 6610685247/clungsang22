#
# FILE: average_2.py
# TASK: average_2
# LANG: PYTHON
# ID:   6610685247
#

input_number = list(map(float, input().split()))

n = 0
Sum = 0

while input_number[n] != -1:
    if 0 <= input_number[n] <= (10**6):
        Sum += input_number[n]
    n += 1
else:
    if n == 0:
        print("0.000")
    else:
        average = Sum / n
        print(f"{average:.3f}")
