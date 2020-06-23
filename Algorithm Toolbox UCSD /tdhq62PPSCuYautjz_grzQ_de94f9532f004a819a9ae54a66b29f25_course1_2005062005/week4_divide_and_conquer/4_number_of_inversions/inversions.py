# Uses python3
import sys

def merge(b,c):
    inversions = b[1] + c[1]
    b = b[0]
    c = c[0]
    result = list()
    while len(b)>0 and len(c)>0:
        if b[0] <= c[0]:
            result.append(b[0])
            del(b[0])
        else:
            result.append(c[0])
            inversions += len(b)
            del(c[0])
    result = result + b
    result = result + c
    return [result, inversions]


def merge_sort(a):
    if len(a) == 1:
        return [a, 0]
    else:
        mid = int((len(a)/2))
        b = merge_sort(a[0: mid])
        c = merge_sort(a[mid: len(a)])
        return merge(b,c)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    result = merge_sort(a)
    print(result[1])
    # print(get_number_of_inversions(a, b, 0, len(a)))
