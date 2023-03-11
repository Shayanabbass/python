def quicksort(a):
    if len(a)<=0:
        return a
    else:
        pivot=a.pop()
    greater=[]
    lower=[]
    for i in a:
        if i> pivot:
            greater.append(i)
        else:
            lower.append(i)  
    return quicksort(lower)+[pivot]+quicksort(greater)        
a=[3,4,6,2,6,8,2,1]
print(quicksort(a))