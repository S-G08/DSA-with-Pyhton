def stockSpan(price, n):
    st=[]
    for i in range(0, n, 1):
        count=1
        j = i - 1
        while (j >= 0) and (price[i] > price[j]):
            count += 1
            j -= 1
        st.append(count)
    return st       
        


price=[60,70,80,100,90,75,80,120]
n=len(price)
output=stockSpan(price, n)
print(output)