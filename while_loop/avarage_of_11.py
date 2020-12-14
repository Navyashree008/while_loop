i=1
total=0
while i<=11:
    weight=int(input("enter weight"))
    i+=1
    total=total+i
print(total)
avarage=total//11
print(avarage)
if avarage%5==0:
    print(avarage,"multiple of 5")
else:
    print("avarage is not multiple of 5")