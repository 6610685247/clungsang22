#
# FILE: next_prime.py
# TASK: next_prime
# LANG: PYTHON
# ID:   6610685247
#


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
    MIN_N = 1
    MAX_N = 10**9

    n = int(input())
    if n < MIN_N or n > MAX_N:
        print("0")
        return
    np = next_prime(n)
    print(f"{np}")


if __name__ == "__main__":
    main()
