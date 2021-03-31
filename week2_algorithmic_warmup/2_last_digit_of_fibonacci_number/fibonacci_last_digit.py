# Uses python3
import sys
import numpy as np


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return str(n)

    prev, curr = 0, 1

    i = 1
    while i < n:
        prev, curr = curr, (prev + curr)
        i = i + 1

    return str(curr)[-1]


def matrixmult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Cannot multiply the two matrices. Incorrect dimensions.")
        return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


def vector_mat_mult(V, M):
    dimensions_V = len(V)
    cols_M = len(M[0])

    C = [0] * dimensions_V

    for k in range(dimensions_V):
        for j in range(cols_M):
            C[k] += V[j] * M[k][j]

    return C


def get_fibonacci_last_digit_mat_exp(n):
    fibs = [0, 1]
    M = [[0, 1], [1, 1]]
    I_n = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            I_n = matrixmult(I_n, M)
        M = matrixmult(M, M)
        n = n // 2

    res = vector_mat_mult(fibs, I_n)

    return str(res[0])[-1]


def get_fibonacci_last_digit_pisano(n):
    # last digit of a num = num % 10
    # pisano period for fib mod 10 = 60
    # i.e. fib_61 mod 10 = fib_1 mod 10 = 1

    fibs = [0, 1]
    for i in range(2, 60):
        fibs.append((fibs[-1] + fibs[-2]) % 10)  # get last digits of first 60 fibs

    return fibs[n % 60]


if __name__ == "__main__":

    n = int(input())
    # print(get_fibonacci_last_digit_mat_exp(n))
    print(get_fibonacci_last_digit_pisano(n))
