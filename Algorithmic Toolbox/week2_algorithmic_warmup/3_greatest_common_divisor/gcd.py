# Uses python3
import sys

def gcd_naive(a,b):
    small = min(a,b)
    big = max(a,b)
    if big%small == 0:
        return small
    else:
        a_prime = big%small
        return gcd_naive(a_prime,small)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))

