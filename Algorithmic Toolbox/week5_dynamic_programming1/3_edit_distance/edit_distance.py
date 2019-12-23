# Uses python3
def edit_distance(s, t):
    A = [[x for x in range(len(t)+1)]]
    for k in range(1,len(s)+1):
        A.append([k]+[0] * len(t))
    for i in range(1,len(A)):
        for j in range(1,len(A[0])):
            if s[i-1] == t[j-1]:
                A[i][j] = A[i-1][j-1]
            else:
                A[i][j]=min(A[i-1][j],A[i][j-1],A[i-1][j-1])+1
    return A[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
