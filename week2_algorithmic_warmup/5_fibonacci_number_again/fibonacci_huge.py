# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):

    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            period = i + 1

    n = n % period
    if n <= 1:
        return n

    fib_0 = 0
    fib_1 = 1
    for fib in range(2, n + 1):
        temp = fib_1
        fib_1 += fib_0
        fib_0 = temp

    return fib_1 % m


if __name__ == "__main__":
    nums = input()
    n, m = nums.split()
    print(get_fibonacci_huge_naive(int(n), int(m)))
