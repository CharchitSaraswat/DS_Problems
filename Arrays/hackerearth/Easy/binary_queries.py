# https://www.hackerearth.com/fr/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/

from sys import stdin, stdout

N_Q = input()
N_Q = N_Q.split()
N = int(N_Q[0])
Q = int(N_Q[1])

input_array = input()
input_array = input_array.split()


for i in range(0, Q):
    query = input()
    query = query.split()
    if query[0] == "1":
        x_bit = int(query[1]) - 1
        if input_array[x_bit] == "0":
            input_array[x_bit] = "1"
        else:
            input_array[x_bit] = "0"
    else:
        x_bit = int(query[2]) - 1
        if input_array[x_bit] == "1":
            print("ODD")
        else:
            print("EVEN")