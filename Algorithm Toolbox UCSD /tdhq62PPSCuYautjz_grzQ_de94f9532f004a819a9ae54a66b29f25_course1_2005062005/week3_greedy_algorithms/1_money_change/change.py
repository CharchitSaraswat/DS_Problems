# Uses python3
import sys

def get_change(m):
    q_10 = int(m / 10)
    r_10 = m % 10
    q_5 = int(r_10/5)
    r_5 = m%5
    return (q_10 + q_5 + r_5) 
    #write your code here

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
