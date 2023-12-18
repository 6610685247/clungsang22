#
# FILE: print_base.py
# TASK: print_base
# LANG: PYTHON
# ID:   6610685247
#


def print_base(n: int, base: int):
    printbase = []
    check = n
    hexadecimal = ["A", "B", "C", "D", "E", "F"]

    remain = check % base
    printbase.append(remain)
    total = check // base
    while total >= base:
        remain = total % base
        printbase.append(remain)
        total //= base
    if total != 0:
        printbase.append(total)

    printbase.reverse()
    if base == 16:
        for index, num in enumerate(printbase):
            if num >= 10:
                new_num = hexadecimal[num - 10]
                printbase[index] = new_num

    for num in printbase:
        print(num, end="")


def main():
    MIN_N = 0
    MAX_N = 1_000_000

    n, base = input().split()
    n = int(n)

    if n < MIN_N or n > MAX_N:
        print("INVALID")
        return
    base = int(base)
    if not (base in [2, 8, 10, 16]):
        print("INVALID")
        return

    print_base(n, base)


main()
