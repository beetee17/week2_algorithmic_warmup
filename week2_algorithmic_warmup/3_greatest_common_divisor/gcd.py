# Uses python3
import sys


def gcd_naive(a, b):

    big = max(a, b)

    small = min(a, b)
    if big % small == 0:
        return small
    return gcd_naive(big % small, small)


if __name__ == "__main__":
    nums = input()
    a, b = nums.split()
    print(gcd_naive(int(a), int(b)))
