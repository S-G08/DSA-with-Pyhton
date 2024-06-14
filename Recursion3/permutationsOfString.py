def permutations(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i, c in enumerate(s):
            for perm in permutations(s[:i] + s[i+1:]):
                perms.append(c + perm)
        return perms


string = input()
ans = permutations(string)
for s in ans:
    print(s)
