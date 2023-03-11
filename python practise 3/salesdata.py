f = open("salesdata.txt","r")
sum1 = 0
f.readline()
for i in f:
    list= i.split()
    sum = int(list[3])*int(list[4])
    sum1+= 0 +sum
print(sum1)    