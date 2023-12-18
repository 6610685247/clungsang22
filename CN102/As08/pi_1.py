#
# FILE: pi_1.py
# TASK: pi_1
# LANG: PYTHON
# ID:   6610685247
#

loopCount = 0
k = 0  # diction count
pi = 0.0

n = int(input())

if not (1 <= n <= 100):
    print("INVALID")
else:
    while loopCount < n:
        pi += ((-1) ** k) / (2 * k + 1)
        k += 1
        loopCount += 1
    pi = pi * 4
    print(f"{pi:.10f}")
