total=0
count=0
avg=0
while True:
    num=input("enter a number")
    if (num=="done"):
        break
    try:
        
        total+=float(num)
        count+=1
        avg=total/count
    except ValueError:
        print("invalid input")  
print(total,count,avg)          


