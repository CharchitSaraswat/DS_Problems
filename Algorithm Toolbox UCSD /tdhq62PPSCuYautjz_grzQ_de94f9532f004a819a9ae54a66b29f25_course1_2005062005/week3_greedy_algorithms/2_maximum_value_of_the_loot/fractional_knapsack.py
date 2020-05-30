# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    value_per_unit = list()
    while capacity:
        max_value_per_unit, index, weight = get_max_value_item(values, weights)
        if not weight:
            break
        if capacity >= weight:
            capacity = capacity - weight
            value += weight * max_value_per_unit
        else:
            value += max_value_per_unit * capacity
            capacity = 0
        del values[index]
        del weights[index]
    return value

def get_max_value_item(values, weights):
    index = -1
    max_value_per_unit = 0
    weight = 0
    if not len(values):
        return max_value_per_unit, index, weight
    for i in range(len(values)):
        if values[i]/weights[i] > max_value_per_unit:
            max_value_per_unit = values[i]/weights[i]
            index = i
            weight =  weights[i]
    return max_value_per_unit, index, weight


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
