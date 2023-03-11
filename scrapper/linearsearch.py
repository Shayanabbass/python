def linearsearch(array,n,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return-1    
array=[1,4,5,6,7,8] 
n=len(array)
x=4
result=linearsearch(array,n,x)
if (result==-1):
    print("element not found")
else:
    print("element found at",result)