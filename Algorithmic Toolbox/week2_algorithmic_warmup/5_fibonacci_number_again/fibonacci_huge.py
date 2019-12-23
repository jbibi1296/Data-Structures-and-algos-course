# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    n %=60
    fib = [0,1]
    for i in range(2,n+1):
        fib.append((fib[i-1])+(fib[i-2]))
    return fib[n]%m
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
