#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    c = list()
    for i in range(len(a)):
        ci = list()
        for j in range(len(b)):
            ci.append(0)
        c.append(ci)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i == 0 or j == 0:
                    c[i][j] = 1
                else:
                    c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return c[len(a) - 1][len(b) - 1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
