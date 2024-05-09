# Given a string S, compute recursively a new string where identical chars that are 
# adjacent in the original string are separated from each other by a "*".
# hello -> hel*lo

def star(str):
    if len(str)<=1:
        return str
    
    new_str=star(str[1:])

    if str[0]==str[1]:
        return (str[0]+"*"+new_str)
    else:
        return (str[0]+new_str)    


str=input()
print(star(str))