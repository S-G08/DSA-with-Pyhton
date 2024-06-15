from os import *
from sys import *
from collections import *
from math import *

# Define a function to find all paths for a rat in a maze
def ratInAMaze(maze, n):
    # Initialize the 'SOLUTION' matrix by all 0s.
    solution = [[0 for j in range(n)] for i in range(n)]

    # Final call to function to print the solutions.
    solveMaze(maze, solution, 0, 0, n)

# Recursive function to solve the maze
def solveMaze(maze, solution, x, y, n):
    # Base case: rat reaches the destination
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        printSolution(solution, n)
        print("")  # Print a newline after each solution
        return

    # Base case: out of boundary of the maze
    if x > n - 1 or x < 0 or y > n - 1 or y < 0:
        return

    # Check if the cell is blocked or already visited
    if maze[x][y] == 0 or solution[x][y] == 1:
        return

    # Mark the cell as visited
    solution[x][y] = 1

    # Explore all possible directions (up, down, left, right)
    solveMaze(maze, solution, x - 1, y, n)  # Up
    solveMaze(maze, solution, x + 1, y, n)  # Down
    solveMaze(maze, solution, x, y - 1, n)  # Left
    solveMaze(maze, solution, x, y + 1, n)  # Right

    # Unmark the cell before backtracking
    solution[x][y] = 0

# Function to print the solution matrix
def printSolution(solution, n):
    for i in range(n):
        for j in range(n):
            print(solution[i][j], end=" ") # Print a newline after each row

# Input the size of the maze

# Main.
n = int(input())
maze = n*[0]

for i in range(0 , n):
    maze[i]=input().split()
    maze[i]=[int(j) for j in maze[i]]
    
ratInAMaze(maze , n) 