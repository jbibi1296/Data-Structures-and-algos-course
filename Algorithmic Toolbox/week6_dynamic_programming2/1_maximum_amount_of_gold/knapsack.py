# Uses python3
import sys

def optimal_weight(W, w):
    value = [[0 for i in range(len(w))]for j in range(W+1)]
    for i in range(len(w)):
        for j in range(W+1):
            value[j][i] = value[j][i-1]
            if w[i] <= j:
                val = value[j-w[i]][i-1]+w[i]
                if value[j][i]< val:
                    value[j][i] = val
    return value[W][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
