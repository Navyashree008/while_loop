# i=1
# while i<=5:
#     j=5
#     while j>=1:
#         print(str(i)*j)
#         j-=1
#         i+=1
#     print()

# i=1
# while i<=5:
#     j=5
#     while j>=1:
#         print(str(i)*j)
#         if i>1:
#             print(" ",str(i)*j)    
#         j-=1
#         i+=1
#     print()

# i=1
# a=0
# while i<=5:
#     print(""*a,end=" ")
#     a+=1
#     j=5
#     while j>=1:
#         print(str(i)*j)
#         j-=1
#     i+=1
# i=0
# while i<=5:
#     print(" "*(i),end=" ")
#     j=5
#     while j>=1:
#         print(str(i)*j,end="")
#         j=j-1
#     print()
#     i=i+1   

i=1
while i<=5:
    j=5
    a=0
    while j>=1:
        print(" "*a,end="")
        print(str(i)*j,end="")
        j-=1
        a+=1
        i+=1
        print()

i=1
while i<=5:
    j=5
    a=0
    while j>=1:
        print(" "*a,end="")
        print("*"*j,end="")
        j-=1
        a+=1
        i+=1
        print()