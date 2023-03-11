number = int(input("enter a number"))
n = 0
i = 2
while(i<=number):
    if (number%i == 0):
        n = 1
    i+=1
if (n == 0):
    print("prime number")
else:
   print ("not a prime number")        