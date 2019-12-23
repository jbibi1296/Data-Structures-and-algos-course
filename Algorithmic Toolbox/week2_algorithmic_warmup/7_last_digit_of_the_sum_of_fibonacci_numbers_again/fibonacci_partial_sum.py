# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to
    from_ %= 1000
    if from_ >= (to % 1000):
        to %= 10000
    else:
        to %= 1000
    fib = []
    for i in range(from_, to + 1):
        fib.append((fib[i-1] % 10)+(fib[i-2] % 10))
    return sum(fib) % 10



if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
