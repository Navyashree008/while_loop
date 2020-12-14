i=1
j=9
num=5
while i<=10:
    guess=int(input("enter no"))
    if guess >=1 and guess<=10:
        if guess == 5:
            print("oohoo u r guess is correct")
            print("won game")
            break
        elif guess<5:
            print("u r guess is less than 5")
        else:
            print('u r guess is greater than 5')
        print("your" + str(j) + "chances are left")
    else:
        print("enter any no between 1 to 10")
    i+=1
    j-=1
else:
    print("sorry you lost game try again")