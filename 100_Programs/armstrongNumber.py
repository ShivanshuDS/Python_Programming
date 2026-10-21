"""
Write a Program of arm strong or not
"""
num=int(input("Enter a Number:-"))
original=num
armnum=0
while num>0:
    digit=num%10
    armnum=armnum+digit**3
    num=num//10;
if original==armnum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong ")