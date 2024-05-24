# For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.

# If the expression can't be balanced, return -1.

def countBracketReversals(s) :
    temp, res, n = 0, 0, len(s)

    if (n % 2 != 0):
        return -1
    for i in range(n):
        if (s[i] == '{'):
            temp += 1
        else:
            if (temp == 0):
                res += 1
                temp += 1
            else:
                temp -= 1

    if (temp > 0):
        res += temp // 2
    return res
st="}{"
print(countBracketReversals(st))
