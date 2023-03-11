num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
num4=int(input("enter a number"))
sum= num1+num3
product= num2*num4
sum1 = sum + 10
product1= product + 20
final_value= sum1*product1
print(final_value)
even= final_value+20
if(final_value%2==0):
    for i in range(final_value,even,2):
        print(i)
elif(final_value%2!=0):
    even2=final_value+1
    for j in range(even2,even,2):
        print(j)

    