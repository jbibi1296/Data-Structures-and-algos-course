# Uses python3
import sys

def get_change(m):
    min_num = [m]*(m+1)
    for i in range(m+1):
        min_num[i]= i
        for coin in [1,3,4]:
            if i>=coin:
                num = min_num[i-coin]+1
                if num<min_num[i]:
                    min_num[i] = num
    return min_num[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
