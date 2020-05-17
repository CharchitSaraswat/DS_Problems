# Uses python3
import sys

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     return a*b
def lcm_eculidean(a, b, gcd):
    return int((a * b)/gcd)


def euclidean_gcd(a, b):
    temp = 0
    if b == 0:
        return a
    temp = a
    a = b
    b = temp % b
    return euclidean_gcd(a, b)

if __name__ == '__main__':
    # input = sys.stdin.read()
    input_console = input()
    a, b = map(int, input_console.split())
    # print(lcm_naive(a, b))
    gcd = euclidean_gcd(a, b)
    print(lcm_eculidean(a, b, gcd))

