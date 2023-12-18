#
# FILE: average_3.py
# TASK: average_3
# LANG: PYTHON
# ID:   6610685247
#

m = int(input())  # count of input line(s)

count = 0
Sum = 0
average = []

for line in range(m):
    input_number = input().split()
    n = int(input_number[0])
    for b in range(1, n + 1):
        Sum += float(input_number[b])
    if n == 0:
        average.append(0.000)
    else:
        average.append(Sum / n)
        Sum = 0

for a in range(m):  # print all output when finished all input
    print(f"{average[a]:.3f}", end="\n")
