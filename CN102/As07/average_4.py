#
# FILE: average_4.py
# TASK: average_4
# LANG: PYTHON
# ID:   6610685247
#

rowCount = 0
n = 0
Sum = 0.0
Avg = []

m = int(input())  # count of input line(s)

if not (0 < m < 20):
    print("Error!")
else:
    while rowCount < m:
        all = input().split()
        for x in all:
            x = float(x)
            if x != -1:
                Sum += x
                n += 1
            else:
                break
        if n == 0:
            Avg.append(0.000)
        else:
            Avg.append(Sum / n)
        Sum = 0.0
        n = 0
        rowCount += 1

    for y in Avg:  # print all output when finished input
        print(f"{y:.3f}", end="\n")
