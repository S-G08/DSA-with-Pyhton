def convert(str):
    if len(str)==1:
        return (ord(str[0])-ord('0'))

    a=convert(str[1:])

    b=ord(str[0])-ord('0')
    b= b * (10**(len(str)-1))+a
    return b

str=input()
print(convert(str))