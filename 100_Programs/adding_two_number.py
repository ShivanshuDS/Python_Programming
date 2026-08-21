# Write a program to add two numbers
#     simple way
num1=int(input("Enter a first number is:-"))
num2=int(input("Enter a Second Number is:-"))
add=num1+num2
print("Adding of two number is:-",add)
print()

    # using function
print("<---------------Using Function---------------->")
number1=int(input("Enter a first number is:-"))
number2=int(input("Enter a second number is:-"))
def add(num1,num2):# create a function
   return num1+num2
print("Adding of two number is:-",add(number1,number2)) # call the function

# using class
class addition:
    def getNumbers(self,number1,number2):
      self.number1=number1
      self.number2=number2
    def operation(self):
       return self.number1+self.number2
calculation=addition()
calculation.getNumbers(32,10)
calculation.operation()