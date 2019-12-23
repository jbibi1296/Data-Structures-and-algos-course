# Uses python3
import sys

def optimal_sequence(n):
    sequence = [0] * (n+1)
    for i in range(1,len(sequence)):
        sequence[i]= sequence[i-1]+1
        if i % 2 ==0:
            sequence[i]= min(sequence[i],sequence[i//2]+1)
        if i % 3 == 0:
            sequence[i]= min(sequence[i],sequence[i//3]+1)
    result = [1] * sequence[-1]
    for i in range(1,sequence[-1]):
        result[-i] = n
        if sequence[n-1] == sequence[n]-1:
            n-=1
        elif n % 2 == 0 and (sequence[n//2]==sequence[n]-1):
            n//=2
        else:
            n//=3
    return result

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
