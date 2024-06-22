

def isValid(adjMatrix, cur, color, col, n):

    for i in range(n):

        if adjMatrix[cur][i] and color[i] == col:
            return False

    return True

def graphColor(adjMatrix, m, cur, color, n):

    if cur == n:
        return True

    for j in range(1, m + 1):

        if isValid(adjMatrix, cur, color, j, n) == True:
            color[cur] = j

            if graphColor(adjMatrix, m, cur+1, color, n):
                return True

            color[cur] = 0

    return False

def graphColoring(adjMatrix, n, m):

    color = [0] * n

    if graphColor(adjMatrix, m, 0, color, n) == True:
        return "Yes"
    
    return "No"