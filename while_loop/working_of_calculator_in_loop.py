num_1=int(input("enter no:"))
num_2=int(input("enter another no:"))
operator=input("enter any operator:")
i=1
if operator =="+":
    var=num_1+num_2
elif operator=="-":
    var=num_1-num_2
elif operator=="*":
    var=num_1 * num_2
elif operator=="/":
    var=num_1/num_2
while i<=var:
    print(i)
    i+=1



