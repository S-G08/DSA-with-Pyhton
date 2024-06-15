ans=[]

def isSafe(row,col,configuration,n):
    for i in range(n):
        for j in range(n):
            if configuration[i][j]==1:
                if col==j:
                    return False
                if (row-col)==(i-j):
                    return False
                if (row+col)==(i+j):
                    return False
    return True

def solve(row, configuration,n):
    global ans
    if row >= n:
        temp_ans=[]
        for i in range(n):
            for j in range(n):
                temp_ans.append(configuration[i][j])
        ans.append(temp_ans)
        return
    for i in range(n):
        if isSafe(row,i,configuration,n):
            configuration[row][i]=1
            solve(row+1,configuration,n)

            #backtrackc=
            configuration[row][i]=0
    return

def solveNQueens(n):
    global ans
    ans=[]
    configuration=[[0 for _ in range(n)]for _ in range(n)]
    solve(0,configuration,n)
    return ans