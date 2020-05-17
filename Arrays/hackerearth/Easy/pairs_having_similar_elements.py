# https: // www.hackerearth.com/fr/practice/data-structures/arrays/1-d/practice-problems/algorithm/pairs-having-similar-element-eed098aa/
from sys import stdin, stdout

N =   int(stdin.readline().strip().split()[0])

input_array = map(int, input().strip().split())

index_similarity = set()

for i in range(len(input_array)):
    if i < len(input_array):
        for j in range(i+1: len(input_array)):
            if input_array[i] == input_array[j] + 1:
                index_similarity.add(str(i)+str(j))
                if 
