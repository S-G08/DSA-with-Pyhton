def subset_sum_to_k_identical(input_arr, k, start=0):
    l=len(input_arr)
    if start >= l:
        return k == 0

    i = start
    sum_val = 0

    while i < l and input_arr[start] == input_arr[i]:
        sum_val += input_arr[i]
        i += 1

    if subset_sum_to_k_identical(input_arr, k - sum_val,i):
        return True

    if subset_sum_to_k_identical(input_arr, k,i):
        return True
    return False

    
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    if subset_sum_to_k_identical(arr, k):
        print("true")
    else:
        print("false")
