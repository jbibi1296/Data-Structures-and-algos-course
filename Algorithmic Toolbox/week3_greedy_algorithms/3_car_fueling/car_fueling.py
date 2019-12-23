# python3
import sys


def compute_min_refills(distance, tank, stops):
    start = 0
    gas_stops = 0
    while distance > (start + tank):
        A = [i for i in stops if i<= (start + tank) and i> start]
        if not A:
            return -1
        else:
            start = max(A)
            gas_stops +=1
    return gas_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
