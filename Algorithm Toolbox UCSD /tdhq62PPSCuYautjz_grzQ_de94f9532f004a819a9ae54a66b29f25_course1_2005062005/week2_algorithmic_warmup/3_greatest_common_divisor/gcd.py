# Uses python3
import sys

# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd

def euclidean_gcd(a, b):
    temp = 0
    if b == 0:
        return a
    temp = a
    a = b
    b = temp % b
    return euclidean_gcd(a, b)

if __name__ == "__main__":
    # input_console = sys.stdin.read()
    input_console = input()
    a, b = map(int, input_console.split())
    # print(gcd_naive(a, b))
    print(euclidean_gcd(a, b))
