def linearSearch(array,x,n):
    for i in array:
        if(array[i]==x):
            return i
    return False    
array=[]
inp=int(input("Enter size of array"))
for i in range(inp):
    numbers=int(input("Enter numbers"))
    array.append(numbers)
x= int(input("enter founding number"))
n= len(array)
result= linearSearch(array,x,n)
if(result==False):
    print("not found")
else:
    print("found at",result)    