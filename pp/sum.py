from ast import Num
num= int(input("entera number"))
num1= int(input("entera number"))
num2= int(input("entera number"))
sum= num+num1+num2
even = sum + 20
if(sum%2==0):
    for i in range(sum,even+1,2):
        print(i)
if(sum%2!=0):
    even2= sum+1
    for j in range(even2,even,2):
        print(j)        
    
    

