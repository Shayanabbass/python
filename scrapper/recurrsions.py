def fn(a,b):
    if b==0:
        return 1
    else:
        return(a*fn(a,b-1))



x=int(input("enter first value")) 
n=int(input("enter second value"))   

y=fn(x,n)
print(y)