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
    
def printKeypad(n,o=""):
    if n==0:
        print(o)
        return 
    smaller_input=n//10
    last_digit=n%10
    output_for_last_digit=keypadalphabets(last_digit)
    
    for c in output_for_last_digit:   
        new_output=c+o
        printKeypad(smaller_input,new_output)   
    
n = int(input())
printKeypad(n)
