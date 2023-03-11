height=float(input("enter your height in centimeters"))
weight=float(input("enter your weight in kg"))
if(weight<(height/2.5)):
    print("you are underweight")
elif((height/2.5)<=weight) and(weight<=(height/2.3)):
    print("you are normal")
elif((height/2.3)<weight):
    print("you are overweight")  
