print("answer in YES or NO")
a= "yes"
b="no"
ques1= input("do you want centigrade to farenheit?")
ques2=input("do you want fareheit to centigrade?")
if (ques1==a and ques2== b):
    C= int(input("please input the temperatutre centigrade"))
    F= 32+C*(9/5)
    print(F)
else:
    print("enter yes or no")
if (ques1==b and ques2== a):
    F= float(input("please input the temperatutre Farenheit"))
    C= (F-32)*5/9
    print(C)
    