def reverseStack(inputStack, extraStack):
    if len(inputStack)<=1:
        return
    while len(inputStack)!=1:
        ele=inputStack.pop()
        extraStack.append(ele)
    
    lastele=inputStack.pop()

    while len(extraStack)!=0:
        ele=extraStack.pop()
        inputStack.append(ele)

    reverseStack(inputStack, extraStack)
    inputStack.append(lastele)

s1=[int(ele) for ele in input().split()]
s2=[]
reverseStack(s1, s2)
while(len(s1)!=0):
    print(s1.pop(),end=" ")
