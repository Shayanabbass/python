def myFunc(x):
    y = x**2 - 5*x +6
    return y
a = float(input("enter the value of lower limit\n"))
b = float(input("enter the value of upper limit\n"))
#x = a
ya = myFunc(a)
#x = b
yb = myFunc(b)
if not ((ya > 0 )and (yb < 0))  or  ((ya < 0) and (yb > 0)) :
    print("solution does not lies between the given range")
else:
    c = (a+b)/2
    #x = c
    yc = myFunc(c)
    while (yc!=0):
            c = (a+b)/2
            #x = c
            yc = myFunc(c)    
            if((ya > 0) and (yc < 0)) or ((ya < 0) and (yc > 0)):
             b = c
            if((yb > 0) and (yc < 0)) or ((yb < 0) and (yc > 0)):
             a = c
    print(c)         
         

        