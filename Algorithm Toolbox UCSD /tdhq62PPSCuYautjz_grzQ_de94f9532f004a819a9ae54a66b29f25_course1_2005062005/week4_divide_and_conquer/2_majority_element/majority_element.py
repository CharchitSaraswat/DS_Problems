# Uses python3
import sys

count_dict = dict()

def get_majority_element(a, left, right):
    if len(a) == 1:
        if a[0] in count_dict.keys():
            count_dict[a[0]] += 1
        else:
            count_dict[a[0]] = 1
        return a
    else:
        mid = int((len(a) - 1)/2)
        get_majority_element(a[0: mid+1], left, right)
        get_majority_element(a[mid+1: len(a)], left, right)
        
    #write your code here
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
    get_majority_element(a, 0, n)
    flag = 0
    for key, value in count_dict.items():
        if value > (len(a)/2):
            flag = 1
            break
    print(flag)
