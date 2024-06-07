import heapq
def getKthLargest(arr, k):
    n = len(arr)

    # Create a prefix sum array.
    prefixSum = [0] * (n + 1)
    for i in range(1, n+1):
        prefixSum[i] = prefixSum[i - 1] + arr[i - 1]

    # Create a heap to store K largest subarray sums.
    subarraySums = []
    heapq.heapify(subarraySums)
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            subarraySum = prefixSum[j] - prefixSum[i]
            if len(subarraySums) < k:
                heapq.heappush(subarraySums, subarraySum)
            else:
                if subarraySum > subarraySums[0]:
                    heapq.heapreplace(subarraySums, subarraySum)

    # Return the K-th largest sum of contiguous subarray.
    return subarraySums[0]