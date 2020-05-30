# Uses python3
import sys

def optimal_summands(n):
    summands = []
    sum_summands = 0
    if n == 0:
        return [0]  
    elif n==1:
        return [1]
    elif n == 2:
        return [2]
    #write your code here
    for i in range(1,n):
        sum_summands += i
        diff = n - sum_summands
        if diff <= i:
            i = i + diff
            sum_summands = n
        summands.append(i)
        if sum_summands == n:
            return summands
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
