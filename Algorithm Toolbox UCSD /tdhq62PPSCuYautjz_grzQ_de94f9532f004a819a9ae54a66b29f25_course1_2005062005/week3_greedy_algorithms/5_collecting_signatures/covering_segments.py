# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    points.append(segments[0].end)
    point = segments[0].end
    i = 0
    while i < len(segments):
        if (point < segments[i].start or point > segments[i].end):
            point = segments[i].end
            points.append(point)
        i += 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments = sorted(segments, key=attrgetter('end'))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
