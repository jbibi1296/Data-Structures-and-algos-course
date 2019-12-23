# python3

import sys
import threading


def compute_height(n,parents):
    cache = [0]*n
    return max([height(i,parents,cache) for i in range(n)])

def height(i, parents,cache):
    if parents[i] == -1:
        return 1
    if cache[i]:
        return cache[i]
    cache[i] = 1 + height(parents[i],parents,cache)
    return cache[i]









def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
