num1 = int(input("enter no:"))
num2 = int(input("enter no:"))
i = 1
while i >=0:
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break
    i+=1
print(lcm)