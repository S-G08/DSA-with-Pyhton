def subsequences(string):
    n=len(string)
    if n==0:
        output=[]
        output.append("")
        return output
    first=string[0]
    smaller_string=string[1:]
    smaller_output=subsequences(smaller_string)
    output=[]
    for ele in smaller_output:
        output.append(ele)
    for ele in smaller_output:
        output.append(string[0]+ele)

    return output

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)