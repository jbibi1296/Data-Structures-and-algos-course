# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    dicc = {values/weights:weights for values,weights in zip(values,weights)}
    for i in sorted(dicc,reverse=True):
        taking = min(capacity,dicc[i])
        value += (i * taking)
        capacity -= taking
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
