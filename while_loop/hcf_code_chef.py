num1 = int(input("enter nu:"))
num2 = int(input("enter no:"))
i = 1
hcf = 0
while i <= 9:
    if num1 % i == 0 and num2 % i ==0:
        a = i
        if a > hcf:
            hcf = a
    i+=1
print(hcf)