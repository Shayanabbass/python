from ast import Num
from tkinter import N
number = int(input("enter the maximum value\n"))
n1 , n2 =0, 1
b = 0
if (b > number ):
    print("please enter a positive integer")
elif(number == 1) :
    print(n1 , n2)       
else:
    while(b < number) :
        print(n1)
        n3 = n1+n2
        n1 = n2
        n2 = n3
      
        b = b + 1 

          
        