def check_id(id: str) -> int:
    a = 0
    b = 0
    c = 0
    x = 0

    for digit in range(13, 1, -1):
        a += digit * int(id[13 - digit])

    b = a % 11
    c = 11 - b
    x = c % 10

    check = int(id[12])
    if x == check:
        return 1
    return 0


def main():
    MIN_N = 0
    MAX_N = 10_000_000_000_000

    id = input()
    n = int(id)

    if len(id) != 13:
        print("INVALID")
        return

    if n < MIN_N or n >= MAX_N:
        print("INVALID")
        return

    res = check_id(id)
    print(res)


main()
