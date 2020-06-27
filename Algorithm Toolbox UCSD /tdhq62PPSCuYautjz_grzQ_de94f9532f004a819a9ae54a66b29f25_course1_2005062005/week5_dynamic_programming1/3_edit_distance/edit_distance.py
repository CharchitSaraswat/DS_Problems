# Uses python3
def edit_distance(a, b):
    #write your code here
    c = list()
    for i in range(len(a)+1):
        ci = list()
        for j in range(len(b)+1):
            ci.append(0)
        c.append(ci)
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0:
                c[i][j] = j
            elif j == 0:
                c[i][j] = i
            elif a[i-1] == b[j-1]:
                c[i][j] = c[i-1][j-1]
            else:
                c[i][j] = 1 + min(c[i][j-1], c[i-1][j], c[i-1][j-1])
    return c[len(a)][len(b)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
