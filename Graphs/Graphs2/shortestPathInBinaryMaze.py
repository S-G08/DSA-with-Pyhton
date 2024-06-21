from queue import Queue

# Check whether given cell (row, col) is a valid cell or not.
def isValid(row, col, ROW, COL):
    # Return true if row number and column number is in range
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


# Function to find the shortest path between a given source cell to a destination cell.
def shortestPathBinaryMatrix(matrix, src, dest):
    ROW = len(matrix)
    COL = len(matrix[0])

    # Check source and destination cell of the matrix have value 1
    if matrix[src[0]][src[1]] != 1 or matrix[dest[0]][dest[1]] != 1:
        return -1

    visited = [[0] * COL for _ in range(ROW)]

    # Mark the source cell as visited
    visited[src[0]][src[1]] = 1

    # Create a queue for BFS
    q = Queue()

    # Distance of source cell is 0
    q.put((src, 0))

    # Do a BFS starting from source cell
    while not q.empty():
        pt, dist = q.get()

        # If we have reached the destination cell, return current distance
        if pt[0] == dest[0] and pt[1] == dest[1]:
            return dist

        # Otherwise dequeue the front cell in the queue and enqueue its adjacent cells
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            row = pt[0] + dx
            col = pt[1] + dy

            # If adjacent cell is valid, has path and not visited yet, enqueue it.
            if isValid(row, col, ROW, COL) and matrix[row][col] == 1 and visited[row][col] == 0:
                # Mark cell as visited and enqueue it
                visited[row][col] = 1
                q.put(((row, col), dist + 1))

    # Return -1, if destination cannot be reached
    return -1
