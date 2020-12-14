num = int(input("enter no:"))
i = 1
sum = 0
while i < num:
    if num % i == 0:
        sum = sum+i
    i+=1
if sum == num:
    print("its a perfect number")
else:
    print("its not a perfect number")