# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    sum_ = 1

    for i in range(2, n + 1):
        prev, curr = curr, (prev + curr)
        sum_ += curr ** 2

    return str(sum_)[-1]


def fibonacci_sum_squares_pisano(n):
    # The figure  represents the sum 𝐹1^2 +𝐹2^2 +𝐹3^2 +𝐹4^2 +𝐹5^2 as the area of a rectangle
    # with vertical side 𝐹5 = 5 and horizontal side 𝐹5 + 𝐹4 = 3 + 5 = 𝐹6
    # Therefore, 𝐹1^2 +𝐹2^2 +𝐹3^2 +... + 𝐹N^2  = 𝐹N * F(N+1)
    # Find last digit of fib(n) and fib(n+1) separately then multiply and mod 10

    fibs = [0, 1]
    for i in range(2, 60):
        fibs.append((fibs[-1] + fibs[-2]) % 10)  # get last digits of first 60 fibs

    return (fibs[n % 60] * fibs[(n + 1) % 60]) % 10


if __name__ == "__main__":

    n = int(input())
    # print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares_pisano(n))
