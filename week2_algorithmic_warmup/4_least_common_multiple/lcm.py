# Uses python3
import sys


def lcm_naive(a, b):
    big = max(a, b)
    small = min(a, b)

    for i in range(1, small + 1):
        if (big * i) % small == 0:
            return big * i


if __name__ == "__main__":
    nums = input()
    a, b = nums.split()
    print(lcm_naive(int(a), int(b)))
