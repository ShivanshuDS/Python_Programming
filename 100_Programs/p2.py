# # WAP to add,sub,mul,division,mod,floor divison,exponential, matrix multiplication
# print("<-------------------without using Function-------------------->")
# num1=float(input("Enter first number is:--"))
# num2=float(input("Enter second number is:-"))
# add=num1+num2
# print("Addition:-",add)
# sub=num1-num2
# print("Subtraction:-",sub)
# mul=num1*num2
# print("Multiplication:-",mul)
# division=num1/num2
# print("division:-",division)
# floor_division=num1//num2
# print("Floor division:-",floor_division)
# mod=num1%num2
# print("Modulus is:-",mod)
# exp=num1**2
# print("Exponential:-",exp)
# import numpy as np
# a=np.array([[1,2],[3,4]])
# b=np.array([[3,5],[2,6]])
# c=a @ b
# print("matrix multiplication:-",c)
# print()

# # using function 
# print("<-------------------Using Function------------------------>")
num1=float(input("Enter first number is:--"))
num2=float(input("Enter second number is:-"))
operation=input("what to do perform the operation:-")
def add(number1,number2):
    return number1+number2
print("Addition:-",add(num1,num2))
def sub(number1,number2):
    return number1-number2
print("Subtraction:-",sub(num1,num2))
def mul(number1,number2):
    return number1*number2
print("Multiplication:-",mul(num1,num2))
def division(number1,number2):
    return number1/number2
print("Division:-",division(num1,num2))
def floorDivision(number1,number2):
    return number1//number2
print("floorDivision:-",floorDivision(num1,num2))
def modulus(number1,number2):
    return number1%number2
print("Modulus:-",modulus(num1,num2))
def exponential(number1,number2):
    return number1**number2
print("Exponential:-",exponential(num1,num2))

# # Using class 
# number1=float(input("Enter a First Number:-"))
# number2=float(input("Enter a Second Number:-"))
# class Calculator:
#     def getNumbers(self,number1,number2):
#         self.number1=number1
#         self.number2=number2
#         # print("First Number is:-",self.number1)
#         # print("Second Number is:-",self.number2)
#     def addition(self):
#         return self.number1+self.number2
#     def subtraction(self):
#         return self.number1-self.number2
#     def multiplication(self):
#         return self.number1*self.number2
#     def division(self):
#         return self.number1/self.number2
#     def floorDivision(self):
#         return self.number1//self.number2
#     def modulus(self):
#         return self.number1%self.number2
#     def exponential(self):
#         return self.number1**self.number2
#     def squareRoot(self):
#         import math
#         return math.sqrt(self.number1)
# obj=Calculator()
# obj.getNumbers(number1,number2)
# print("Addition:-",obj.addition())
# print("Substraction:-",obj.subtraction())
# print("Division:-",obj.division())
# print("Floor_Division:-",obj.floorDivision())
# print("Modulus:-",obj.modulus())
# print("Exponential:-",obj.exponential())
# print("Square_Root:-",obj.squareRoot())