#
# FILE: pi_2.py
# TASK: pi_2
# LANG: PYTHON
# ID:   6610685247
#

loopCount = 0
loop_in_pi = 0.0

n = int(input())

if not (1 <= n <= 100):
    print("INVALID")
else:
    if n == 1:  # 1n mean just diction "3"
        loop_in_pi = 0.0
    else:
        while loopCount < n - 1:
            loop_in_pi += ((-1) ** loopCount) / (
                ((2 * loopCount) + 2) * ((2 * loopCount) + 3) * ((2 * loopCount) + 4)
            )
            loopCount += 1
    pi = 3 + (4 * loop_in_pi)
    print(f"{pi:.10f}")
