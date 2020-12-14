# i=1
# while i<=5:
#     j=5
#     while j>=1:
#         print(" "*i,end="")
#         print("* "*j,end="")
#         j-=1
#         i+=1
#         print()

# i=1
# while i<=5:
#     j=5
#     while j>=1:
#         print(" "*j,end="")
#         print("* "*i,end="")
#         j-=1
#         i+=1
#         print()


# i=1
# while i<=5:
#     j=5
#     while j>=1:
#         print(" "*j,end="")
#         print("* "*i,end="")
#         j-=1
#         i+=1
        
#         print()
#         if i==5:
#             i=1
#             while i<=5:
#                 j=5
#                 while j>=1:
#                     print(" "*i,end="")
#                     print("* "*j,end="")
#                     j-=1
#                     i+=1
#                     print()

# i=65
# ch=chr(i)
# print(ch)

a=1
i=65
ch=chr(i)
while i<=70:
    j=5
    while j>=1:
        print(" "*j,end="")
        print(str(ch)*a,end=" ")
        i+=1
        j-=1
        a+=1
        print()
        if a==5:
            i=70
            ch=chr(i)
            while i>=65:
                j=5
                while j>=1:
                    print(" "*a,end="")
                    print(str(i)*j,end="")
                    i-=1
                    j-=1
                    a-=1
                    print()



