a=int(input("enter the no:"))
b=int(input("enter another no:"))
lcm=2
d=1
i=2
while i<=a:
    if a% i==0 or b%i==0:
        lcm=i
        d=d*lcm
    i+=1
print(d)

# a=1234
# print(a[1])