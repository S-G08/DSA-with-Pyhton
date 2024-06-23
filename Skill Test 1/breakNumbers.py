import sys

# Output a partition
def output_partition(n, x):
    for i in range(1, n+1):
        # Can't show negative numbers
        if x[i] > 0:
            if i == n:
                print(x[i], end=" ")
            else:
                print(x[i], end=" ")
    print()

# This is the function which generates the partitions of a given number "n"
def generate_partitions(x, n):
    k, s = 1, 0  # s represents the sum of already-generated components
    # Initialize the solution vector's elements with -1
    for k in range(1, n):
        x[k] = -1
    k = 1
    while k > 0:
        # Generated a solution, let's output it then
        if k == n:
            x[n] = n - s
            output_partition(n, x)
            k -= 1
            s -= x[k]
        else:
            # Check for another solution
            if ((n - k + 1) * (x[k] + 1)) <= n - s:
                x[k] += 1
                if x[k] >= x[k - 1]:
                    s += x[k]
                    k += 1
            else:
                # Didn't find any solutions, reset x[k] to -1
                x[k] = -1
                k -= 1
                s -= x[k]

# Test
if __name__ == "__main__":
    number = int(input())
    x = [-1] + [0] * number
    # print(number)
    generate_partitions(x, number)
    

