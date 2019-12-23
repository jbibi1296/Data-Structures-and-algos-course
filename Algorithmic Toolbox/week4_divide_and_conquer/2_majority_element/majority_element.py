# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (left + right - 1)//2 + 1
    left_a = get_majority_element(a,left,mid)
    right_a = get_majority_element(a,mid,right)
    left_count = 0
    right_count = 0
    for i in range(left,right):
        if a[i] == left_a:
            left_count +=1
        if a[i] == right_a:
            right_count +=1
    if left_count > (right-left)//2:
        return left_a
    if right_count > (right-left)//2:
        return right_a
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
