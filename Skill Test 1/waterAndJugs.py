def canMeasureWater(x: int, y: int, z: int) -> bool:
    def dfs(i: int, j: int) -> bool:
        if (i, j) in vis:
            return False
        vis.add((i, j))
        if i == z or j == z or i + j == z:
            return True
        if dfs(x, j) or dfs(i, y) or dfs(0, j) or dfs(i, 0):
            return True
        a = min(i, y - j)
        b = min(j, x - i)
        return dfs(i - a, j + a) or dfs(i + b, j - b)

    vis = set()
    return dfs(0, 0)

t=int(input())
# a=[]
# b=[]
# c=[]
for i in range(t):
    li=[int(ele) for ele in input().split()]
    # a.append(li[0])
    # b.append(li[1])
    # c.append(li[2])

    ans=canMeasureWater(li[0],li[1],li[2])
    if ans:
        print("Yes")
    else:
        print("No")