# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    fib = [0,1]
    n = n%1000
    for i in range(2,n+1):
        fib.append((fib[i-1]%10)+(fib[i-2]%10))
    return sum(fib)%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
