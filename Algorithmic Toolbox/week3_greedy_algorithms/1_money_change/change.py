# Uses python3
import sys

def get_change(m):
    num = m
    m = 0
    for i in [10,5,1]:
        m+=(num//i)
        num %= i
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
