n = int(input("enter no:"))
while n>0:
    a = n//10
    if a%10==7:
        print("yes")
    else:
        print("no")
    n=n-n