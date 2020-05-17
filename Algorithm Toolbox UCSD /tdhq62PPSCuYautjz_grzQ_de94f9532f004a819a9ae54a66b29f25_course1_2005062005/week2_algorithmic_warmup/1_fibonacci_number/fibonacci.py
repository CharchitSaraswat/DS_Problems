# Uses python3
# def calc_fib(n):
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)
def calc_fib(n):
    fib_seq = [0, 1]
    if n == 0:
        return fib_seq[0] 
    for i in range(2, n+1):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[-1]

n = int(input())
print(calc_fib(n))
