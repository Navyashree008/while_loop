# x=0
# y=1
# while x<=100:
#     print(x)
#     z=x
#     x=y
#     y=z+y


n = int(input('enter no'))
y = 1
x = 0
while x <= n:
    print(x)
    z = x
    x = y
    y = z+y