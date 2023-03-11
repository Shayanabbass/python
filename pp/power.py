plus="+"
minus="-"
multiply="*"
divide="/"
n1= int(input("enter first number"))
n2=int(input("enter second number"))
operator = input("enter operator")
if(operator== plus):
    ans=n1+n2
    print(ans)
elif(operator== minus):
    ans=n1-n2
    print(ans)
elif(operator== multiply):
    ans=n1*n2
    print(ans) 
elif(operator== divide):
    ans=n1/n2
    print(ans)       