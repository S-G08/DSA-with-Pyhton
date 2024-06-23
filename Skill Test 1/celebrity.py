
def celebrity( M, n):
    # code here
    i = 0
    j = n-1
    candidate = -1
    while(i < j):
        if M[j][i] == 1:
            j -= 1
        else:
            i += 1

    candidate = i
    for k in range(n):
        if candidate != k:
            if M[candidate][k] == 1 or M[k][candidate] == 0:
                return -1

    return candidate

n=int(input())
input_line = input()
values_str = input_line.split()
mat = [[int(values_str[j + i * n]) for j in range(n)] for i in range(n)]


a = celebrity(mat, n)
if a == -1:
    print("No Celebrity")
else:
    print("Celebrity ID", a)
