# python3
import sys


def compute_min_refills(distance, tank, stops, _):
    # write your code here
    min_stops = int(distance/tank) - 1
    refuelling_stop = 0
    num_stops = 0
    if _ < min_stops:
        return -1
    if distance - stops[-1] > tank:
        return -1
    if distance < tank:
        return num_stops
    for i in range(len(stops)):
        if i == 0:
            diff = stops[0]
        else:
            diff = stops[i] - stops[i-1]
        if diff > tank:
            return -1
        else:
            if i != len(stops) - 1:
                if (stops[i+1] - refuelling_stop) > tank:
                    refuelling_stop = stops[i]
                    num_stops += 1
            else:
                if (distance - refuelling_stop) > tank:
                    refuelling_stop = stops[i]
                    num_stops += 1
    return num_stops
    
    

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d, m, _, stops = 5, 1, 4, [1,2,3,4]
    print(compute_min_refills(d, m, stops, _))
