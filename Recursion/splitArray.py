# Given an integer array A of size N, check if the input array can be divided in two groups G1 and G2 with following properties-

# - Sum of both group elements are equal
# - Group 1: All elements in the input, which are divisible by 5 
# - Group 2: All elements in the input, which are divisible by 3 (but not divisible by 5). 
# - Elements which are neither divisible by 5 nor by 3, can be put in either group G1 or G2 to satisfy the equal sum property. 
# Group 1 and Group 2 are allowed to be unordered and all the elements in the Array A must belong to only one of the groups.



# Return true, if array can be split according to the above rules, else return false.

def check(arr, n, s, l, r):
    if (s==n):
        return l==r
    
    if (arr[s]%5==0):
        l+=arr[s]
    elif (arr[s]%3==0):
        r+=arr[s]
    
    else:
        return (check(arr,n,s+1,l+arr[s],r) or check(arr, n ,s+1,l,r+arr[s]))
    
    return check(arr,n,s+1,l,r)



def split_array(input, size):
    return check(input,size,0,0,0)


def main():
    size = int(input())
    input_array = list(map(int, input().split()))

    if split_array(input_array, size):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
