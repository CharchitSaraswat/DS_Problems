# Uses python3
import sys

def get_sequence(min_no_ops, n):
    sequence = list()
    while n > 1:
        sequence.insert(0, n)
        if n % 3 == 0 and min_no_ops[n] == min_no_ops[n/3] + 1:
            n = n//3
        elif n % 2 == 0 and min_no_ops[n] == min_no_ops[n/2] + 1:
            n = n//2
        elif min_no_ops[n] == min_no_ops[n - 1] + 1:
            n = n - 1
    sequence.insert(0, 1)
    return sequence

def optimal_sequence(n):
    sequence = []
    min_no_ops = dict()
    min_no_ops[1] = 0
    min_no_ops[2] = 1
    min_no_ops[3]  =1
    for num in range(4, n+1):
        min_no_ops[num] = 1000000
        num_ops_3 = 1000000
        num_ops_2 = 1000000
        if num % 3 == 0:
            num_ops_3 = min_no_ops[num/3] + 1
        elif num % 2 == 0:
            num_ops_2 = min_no_ops[num/2] + 1
        num_ops_1 = min_no_ops[num-1] + 1
        min_no_ops[num] = min(num_ops_1, num_ops_2, num_ops_3)
    sequence = get_sequence(min_no_ops, n)
    return sequence
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
