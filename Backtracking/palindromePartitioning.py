from typing import List
def partition(s: str):
    def dfs(start_index: int):
        if start_index == length:
            result.append(current_partition[:])  
            return
        for end_index in range(start_index, length):
            if palindrome_flags[start_index][end_index]:
                current_partition.append(s[start_index:end_index + 1])
                dfs(end_index + 1)
                current_partition.pop()  
    length = len(s)
    palindrome_flags = [[True] * length for _ in range(length)]
    for i in range(length - 1, -1, -1):
        for j in range(i + 1, length):
            palindrome_flags[i][j] = s[i] == s[j] and palindrome_flags[i + 1][j - 1]
    result = []
    current_partition = []
    dfs(0)     
    return result

s="BaaB"
print(partition(s))