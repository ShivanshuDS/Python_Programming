# Enter three different value find out the greatest one by using nested if method.
a=int(input("Enter a first number is:-"))
b=int(input("Enter a second number is:-"))
c=int(input("Enter a Third number is:-"))
if a>b:
    if a>c:
        print("a is greater")
elif b>c:
    if b>a:
        print("b is greater")
else:
    print("c is greater")