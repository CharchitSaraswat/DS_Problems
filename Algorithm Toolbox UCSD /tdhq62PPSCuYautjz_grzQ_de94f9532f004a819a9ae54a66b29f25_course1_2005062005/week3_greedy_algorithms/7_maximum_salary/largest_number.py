#Uses python3

import sys

def is_greater_or_equal(digit, number):
    if not number:
        number = ""
    front_append = int(str(digit) + str(number))
    back_append = int(str(number) + str(digit))
    if front_append >= back_append:
        return True
    else:
        return False

def largest_number(digits):
    #write your code here
    res = ""
    while digits:
        max_digit = 0
        for digit in digits:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        res += str(max_digit)
        digits.remove(max_digit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
