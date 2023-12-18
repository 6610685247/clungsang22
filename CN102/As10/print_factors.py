#
# FILE: print_factors.py
# TASK: print_factors
# LANG: PYTHON
# ID:   6610685247
#


def print_factors(x):
    div = 2
    while x != 1:
        if x % div == 0:
            print(f"{div}", end="")
            x //= div

            if x != 1:
                print(" x ", end="")
        else:
            div = next_prime(div)


def next_prime(n):
    prime = []
    count = 0
    for a in range(n, 10**9):
        if is_prime(a):
            prime.append(a)
            count += 1

        if count == 2:
            break

    if is_prime(n):
        return prime[1]
    else:
        return prime[0]


def is_prime(num):
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0:
        return False
    else:
        prime = 0
        for div in range(3, num, 2):
            if num % div == 0:
                prime = 0
                return False
            else:
                prime = 1

        if prime == 1:
            return True


def main():
    MIN_N = 2
    MAX_N = 10000

    n = int(input())
    if n < MIN_N or n > MAX_N:
        print("0")
        return
    print_factors(n)


main()
