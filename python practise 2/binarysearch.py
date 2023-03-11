def binarySearch(array,x,high,low):
    while(low<=high):
        mid=(low+high)//2
        if(array[mid]==x):
            return mid
        elif(array[mid]<x):
            low= mid+1
        else:
            high= mid-1
    return False                





array= [1,3,4,5,6,8] 
x= 8
low=0
high=len(array)-1
result=binarySearch(array,x,high,low)
if(result==False):
    print("not found")
else:
    print("found at index",result)     
