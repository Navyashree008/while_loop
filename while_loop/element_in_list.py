list1=[12,15,32,42,55,75,122,132,150,180,200]
a=len(list1)
i=1
while i<=a:
    if i%5==0:
        print(i)
    if i>=150:
        break
    i+=1