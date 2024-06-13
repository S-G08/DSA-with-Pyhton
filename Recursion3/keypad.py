def keypadalphabets(n):
    if n==2:
        return "abc"
    elif n==3:
        return "def"
    elif n==4:
        return "ghi"
    elif n==5:
        return "jkl"
    elif n==6:
        return "mno"
    elif n==7:
        return "pqrs"
    elif n==8:
        return "tuv"
    elif n==9:
        return "wxyz"
    return " "
    
def keypad(n):
    if n==0:
        output=[]
        output.append("")
        return output
    smaller_input=n//10
    last_digit=n%10
    smaller_output=keypad(smaller_input)
    output_for_last_digit=keypadalphabets(last_digit)
    output=[]
    for s in smaller_output:
        for c in output_for_last_digit:   
            option=s+c
            output.append(option)        
    return output
n = int(input())
ans = keypad(n)
for s in ans:
    print(s)