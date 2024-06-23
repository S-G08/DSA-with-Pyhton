


def findDiagonalOrder(mat):
    m, n = len(mat), len(mat[0])
    ans = []
    for k in range(m + n - 1):
        t = []
        i = 0 if k < n else k - n + 1
        j = k if k < n else n - 1
        while i < m and j >= 0:
            t.append(mat[i][j])
            i += 1
            j -= 1
        if k % 2 == 0:
            t = t[::-1]
        ans.extend(t)
    for ele in ans:
        print(ele,end=" ")

mat = [[ 1, 2, 3, 4 ], 
	[ 5, 6, 7, 8 ], 
	[ 9, 10, 11, 12 ], 
	[ 13, 14, 15, 16 ],
    [17,18,19,20]]
ans=findDiagonalOrder(mat)

		

