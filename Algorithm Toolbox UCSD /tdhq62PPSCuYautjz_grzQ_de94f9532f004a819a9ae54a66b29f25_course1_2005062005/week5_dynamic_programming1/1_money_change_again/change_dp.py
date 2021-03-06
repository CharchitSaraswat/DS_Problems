# Uses python3
import sys

def get_change(m):
    #write your code here
    denominations = [1, 3, 4]
    min_num_coins = dict()
    min_num_coins[0] = 0
    for money in range(1, m+1):
        min_num_coins[money] = 10000000
        for coin in denominations:
            if money >= coin:
                num_coins = min_num_coins[money - coin] + 1
                if num_coins < min_num_coins[money]:
                    min_num_coins[money] = num_coins
    return min_num_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
