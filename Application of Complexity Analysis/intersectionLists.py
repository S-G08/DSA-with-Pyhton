#Intersection of two lists 
def intersection(a,b):
    i=0
    j=0
    while i<len(a) and j<len(b):
        if (a[i]<b[j]):
            i+=1
        elif (a[i]>b[j]):
            j+=1
        else:
            print(a[i],end=' ')
            i+=1
            j+=1

a1=[6,9,8,5]
a2=[9,2,4,1,2,8]
if(len(a1)<=len(a2)):
    a1.sort()
    a2.sort()
    intersection(a1,a2)
else:
    a1.sort()
    a2.sort()
    intersection(a2,a1)

    

