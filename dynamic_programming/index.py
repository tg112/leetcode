memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

def fib2(n):
    if n == 0:
        return 0

    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n]

# メモリ最適化
def fib_optimized(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b
