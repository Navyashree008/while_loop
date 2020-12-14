i=1
j = 4
num=5
while i<=5:
    guess=int(input("enter no"))
    if guess>=1 and guess<=10:
        if guess == num:
            print("oohoo")
            print("won game")
            break
        print("your"+ str(j) +"chances are left")
        i+=1  
        j = j-1
    else:
        print("enter any no b/w 1 to 10") 
else:
    print("sorry u lost game try again")
