# Uses python3
def calc_fib(n):

    if n < 1:
        return n

    fib_0 = 0
    fib_1 = 1
    for fib in range(2, n + 1):
        temp = fib_1
        fib_1 += fib_0
        fib_0 = temp

    return fib_1


n = int(input())
print(calc_fib(n))
