# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.

def staircase(n):
    if n<=3:
        if n==1:
            return 1
        if n==2:
            return 2
        else:
            return 4
    a=staircase(n-1)
    b=staircase(n-2)
    c=staircase(n-3)
    return a+b+c
    
n=int(input())
print(staircase(n))