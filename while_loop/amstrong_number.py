n=int(input("enter no"))
k=n
b=n
count=0
while n>0:
    count+=1
    n=n//10
#print(count)
c=str(b)
sum=0
i=0
while i<count:
    print(c[i])
    num=c[i]
    i+=1
    s=int(num)
    power=s**count
    #print(power)
    sum=sum+power
#print(sum)
if n==sum:
    print("its a amstong number")
else:
    print("its not a amstrong numbner")