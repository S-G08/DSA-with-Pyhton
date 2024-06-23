
M = 1000000007

def count_binary_strings(n, k):
	dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n + 1)] 
	dp[1][0][0] = 1
	dp[1][0][1] = 1

	for i in range(2, n + 1):
		for j in range(k + 1):
			dp[i][j][0] = ((dp[i - 1][j][0] % M) + (dp[i - 1][j][1] % M)) % M
			dp[i][j][1] = (dp[i - 1][j][0]) % M
			if j - 1 >= 0: 
				dp[i][j][1] += (dp[i - 1][j - 1][1]) % M 

	return ((dp[n][k][0] % M) + (dp[n][k][1] % M)) % M

# Driver code 
if __name__ == "__main__": 
	t = int(input())
	while t > 0:
		j, k = map(int, input().split())
		print(count_binary_strings(j, k))
		t -= 1