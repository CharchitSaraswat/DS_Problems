# Uses python3
import sys


def get_pisano_period(n, m):
    if n <= 1:
        return None

    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current % m, (previous % m) + (current % m)
        if previous == 0 and current == 1:
            return _ + 1

def calc_fib(n):
    fib_seq = [0, 1]
    if n == 0:
        return fib_seq[0]
    for i in range(2, n+1):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[-1]

if __name__ == '__main__':
    # input = sys.stdin.read();
    console_input = input()
    n, m = map(int, console_input.split())
    pisano_period = get_pisano_period(n, m)
    if pisano_period:
        print(calc_fib(n % pisano_period) % m)
    else:
        print(calc_fib(n) % m)
