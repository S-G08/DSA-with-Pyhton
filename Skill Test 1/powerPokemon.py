import sys
from collections import defaultdict

MOD = 1000000007

def count_pairs(arr):
    count_map = defaultdict(int)
    n = len(arr)
    res = 0
    for num in arr:
        power = 1
        for _ in range(22):
            if (power - num) in count_map:
                res += count_map[power - num]
                res %= MOD
            power *= 2
        count_map[num] += 1
    return res

if __name__ == "__main__":
    n=int(input())
    li=[int(ele) for ele in input().split()]
    ans=count_pairs(li)
    print(ans)


