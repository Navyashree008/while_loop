i=2
a=int(input("enter no"))
wlile i<=100:
    while i<=a-1:
        if a%i==0:
            print("not a prime no")
            break
        i+=1
    else:
        print("its a prime no")
else:
    print("its more than 100")