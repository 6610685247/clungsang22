#
# FILE: secret.py
# TASK: secret
# LANG: PYTHON
# ID:   6610685247
#

n = int(input())

all_missing = []

while n != 0:
    count = 0
    sum_num = 0
    missing = 0
    lim = 0
    while count < n - 1:
        count += 1
        num = int(input())
        sum_num += num

    for a in range(n + 1):
        lim += a

    missing = lim - sum_num
    all_missing.append(missing)

    n = int(input())

for a in all_missing:
    print(f"{a}")
