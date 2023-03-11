sum=0
subjects= 6
tm= int(input("enter total marks"))
for i in range(0,6):
    marks=int(input("enter your marks"))
    sum+=marks
per= (sum/tm)*100
print("your percentage is",per)
if(per>=90):
    print("you scored GRADE A")  
elif(per>=80 and per<=89):
    print("you scored GRADE B+")
elif(per>=70 and per<=79):
    print("you scored GRADE B")
elif(per>=60 and per<=69):
    print("you scored GRADE c")  
else:
    print("you failed")      

    