# Uses python3
from sys import stdin


def calc_sum_pisano_fib(pi):
    prev = 0
    curr = 1
    sum_last_dig = 1
    for _ in range(2, pi):
        prev, curr = curr % 10, (prev + curr) % 10
        sum_last_dig += curr
    return sum_last_dig % 10


def calc_sum_last_dig(rem):
    if rem <= 1:
        return rem
    prev = 0
    curr = 1
    for _ in range(2, rem+1):
        prev, curr = curr % 10, (prev + curr) % 10
    return curr % 10

def get_last_dig_n_fib(n, sum_last_dig_pisano):
    pisano_period =  60
    q = int(n/pisano_period)
    r = n % pisano_period
    last_dig_fib = 0
    last_dig_fib = (last_dig_fib + q*sum_last_dig_pisano) % 10
    last_dig_fib = (last_dig_fib + calc_sum_last_dig(r)) % 10
    return last_dig_fib

def fibonacci_sum_squares(n, sum_last_dig_pisano):
    fn = get_last_dig_n_fib(n, sum_last_dig_pisano)
    fn_1 = get_last_dig_n_fib(n+1, sum_last_dig_pisano)
    return (fn*fn_1)%10

if __name__ == '__main__':
    # n = int(stdin.read())
    n = int(input())
    sum_last_dig_pisano = calc_sum_pisano_fib(60)
    print(fibonacci_sum_squares(n, sum_last_dig_pisano))
