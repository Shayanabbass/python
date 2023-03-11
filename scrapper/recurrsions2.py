


def rec(a,b):
    if (b==0):
        return 1
    elif(b<0):
        return (1/a * rec(a,b+1))
    else:
        return (a * rec(a,b-1))


a = int(input("enter nmuber"))  
b=int(input("enter power"))
y=rec(a,b)
print(y)

