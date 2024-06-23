from string import ascii_lowercase as asc_lower
def checkPangram(s):
    return set(asc_lower)-set(s.lower()) == set([])

#main
n=int(input())
s=input()
if checkPangram(s):
    print("YES")
else:
    print("NO")

