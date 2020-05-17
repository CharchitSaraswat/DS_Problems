# Uses python3
import sys

def calc_sum_last_dig(rem):
    if rem <= 1:
        return rem
    prev = 0
    curr = 1
    sum_last_dig = 1
    for _ in range(2,rem+1):
        prev, curr = curr % 10, (prev + curr) % 10
        sum_last_dig += curr
    return sum_last_dig%10

def calc_sum_pisano_fib(pi):
    prev = 0
    curr = 1
    sum_last_dig = 1
    for _ in range(2, pi):
        prev, curr = curr % 10, (prev + curr) % 10
        sum_last_dig += curr
    return sum_last_dig%10

def fibonacci_sum_pisano(n):
    pisano_period_10 = 60
    sum_pisano_fib = calc_sum_pisano_fib(pisano_period_10)
    q = int(n/pisano_period_10)
    r = n % pisano_period_10
    sum_last_digit = 0
    sum_last_digit = (sum_last_digit + (q * sum_pisano_fib))%10
    sum_last_digit = (sum_last_digit + calc_sum_last_dig(r))%10
    return sum_last_digit

if __name__ == '__main__':
    # input = sys.stdin.read()
    console_input = input()
    n = int(console_input)
    print(fibonacci_sum_pisano(n))
    # fibonacci_sum_pisano(n)
