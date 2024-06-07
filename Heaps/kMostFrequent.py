from typing import List

def KMostFrequent(n: int, k: int, nums: List[int]) -> List[int]:
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
    result = []
    i = 0
    for num, count in freq.items():
        result.append(num)
        i += 1
        if i == k:
            break
        
    return result
