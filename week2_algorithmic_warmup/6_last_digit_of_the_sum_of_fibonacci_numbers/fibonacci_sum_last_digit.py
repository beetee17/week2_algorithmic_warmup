# Uses python3
import sys


def fibonacci_sum_naive(n):

    # fibs = [0, 1]
    # for i in range(2, n + 1):
    #     fibs.append(fibs[-1] + fibs[-2])
    # return str(sum(fibs) % 10)
    if n <= 1:
        return n

    prev, curr = 0, 1
    sum_ = 1

    for i in range(2, n + 1):
        prev, curr = curr, (prev + curr)
        sum_ += curr

    return str(sum_)[-1]


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


def fibonacci_sum_mat_exp(n):
    if n <= 1:
        return n

    initial = [0, 1, 1]  # Vector of [fib0, fib1, sum1]
    M = [[0, 1, 0], [1, 1, 0], [1, 1, 1]]  # inital * M = [fib1, fib2, sum2] ...
    I_n = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Identity matrix such that I_n * M = M
    n -= 1  # product of initial vector and matrix raised to n-1 exponent gives the sum of first n terms

    while n > 0:
        if n % 2 == 1:
            I_n = matrixmult(I_n, M)
        M = matrixmult(M, M)
        n = n // 2

    res = vector_mat_mult(initial, I_n)

    return str(res[-1] % 10)


def fibonacci_sum_n_minus_2(n):
    fibs = [0, 1]
    M = [[0, 1], [1, 1]]
    I_n = [[1, 0], [0, 1]]

    n += 2  # sum of first n terms is fib(n+2) - 1

    while n > 0:
        if n % 2 == 1:
            I_n = matrixmult(I_n, M)
        M = matrixmult(M, M)
        n = n // 2

    res = vector_mat_mult(fibs, I_n)

    return str(res[0] - 1)[-1]


def fibonacci_sum_pisano(n):
    # last digit of a num = num % 10
    # pisano period for fib mod 10 = 60
    # i.e. fib_61 mod 10 = fib_1 mod 10 = 1
    # sum of first n terms is fib(n+2) - 1
    # therefore, last digit of sum to nth term = [(fib(n+2) - 1] mod 10 = fib(n+2) mod 10 - 1

    fibs = [0, 1]
    for i in range(2, 60):
        fibs.append((fibs[-1] + fibs[-2]) % 10)  # get last digits of first 60 fibs

    res = fibs[(n + 2) % 60] - 1
    if res == -1:
        res = 9

    return res


if __name__ == "__main__":

    n = int(input())
    print(fibonacci_sum_pisano(n))
    # print(fibonacci_sum_mat_exp(n))
