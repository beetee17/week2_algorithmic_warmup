# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    fibs = [0, 1]

    for i in range(2, to + 1):
        fibs.append(fibs[i - 2] + fibs[i - 1])
    print(sum(fibs[:]), sum(fibs[:from_]))
    return str(sum(fibs[: to + 1]) - sum(fibs[:from_]))[-1]


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


def fibonacci_partial_sum_mat_exp(from_, to):
    if to == 1:
        return to
    if from_ <= 1:
        from_res = [0, 0, from_]
    else:
        from_ -= 2  # product of initial vector and matrix raised to n-1 exponent gives the sum of first n-1 terms
        initial = [0, 1, 1]  # Vector of [fib0, fib1, sum1]
        M = [[0, 1, 0], [1, 1, 0], [1, 1, 1]]  # inital * M = [fib1, fib2, sum2] ...
        I_n = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Identity matrix such that I_n * M = M

        while from_ > 0:
            if from_ % 2 == 1:
                I_n = matrixmult(I_n, M)
            M = matrixmult(M, M)
            from_ = from_ // 2

        from_res = vector_mat_mult(initial, I_n)

    initial = [0, 1, 1]  # Vector of [fib0, fib1, sum1]
    M = [[0, 1, 0], [1, 1, 0], [1, 1, 1]]  # inital * M = [fib1, fib2, sum2] ...
    I_n = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Identity matrix such that I_n * M = M

    to -= 1  # product of initial vector and matrix raised to n-1 exponent gives the sum of first n terms
    while to > 0:
        if to % 2 == 1:
            I_n = matrixmult(I_n, M)
        M = matrixmult(M, M)
        to = to // 2

    to_res = vector_mat_mult(initial, I_n)
    print(to_res[-1], from_res[-1])
    return str((to_res[-1] - from_res[-1]) % 10)


def fibonacci_partial_sum_pisano(from_, to):
    # last digit of a num = num % 10
    # pisano period for fib mod 10 = 60
    # i.e. fib_61 mod 10 = fib_1 mod 10 = 1
    # last digit of partial sum (m to n) = sum of last digits from mth to nth term
    # sum of last digits also follow the pisano period. i.e. sum of last digits from 0 to 119 = 0 to 59

    fibs = [0, 1]
    for i in range(2, 60):
        fibs.append((fibs[-1] + fibs[-2]) % 10)  # get last digits of first 60 fibs
    from_ = from_ % 60
    to = from_ + (to - from_) % 60
    # to - from_ = number of values between from and to
    # mod 60 as only first cycle through pisano period is required
    sum = 0

    for i in range(from_, to + 1):
        if i >= 60:
            i = i % 60  # end of period reached, return to the start
        sum += fibs[i]

    return sum % 10


if __name__ == "__main__":

    nums = input()
    from_, to = nums.split()
    # print(fibonacci_partial_sum_naive(int(from_), int(to)))
    # print(fibonacci_partial_sum_mat_exp(int(from_), int(to)))
    print(fibonacci_partial_sum_pisano(int(from_), int(to)))
