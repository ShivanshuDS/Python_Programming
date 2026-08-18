# using function,if-elif-else,while loop
'''
def add(number1,number2):
    return number1+number2
def sub(number1,number2):
        return number1-number2
def mul(number1,number2):
        return number1*number2
def division(number1,number2):
        return number1/number2
def floorDivision(number1,number2):
        return number1//number2
def modulus(number1,number2):
        return number1%number2
def exponential(number1,number2):
    return number1**number2
while True:
    num1=float(input("Enter first number is:--"))
    num2=float(input("Enter second number is:-"))
    operation=input("Choose_Your_Operation(+,-,*,/,//,%,**):-")
    if "+"==operation:
        print("Addition:-",add(num1,num2))
    elif "-"==operation:
        print("Subtraction:-",sub(num1,num2))
    elif "*"==operation:
        print("Multiplication:-",mul(num1,num2))
    elif "/"==operation:
        print("Division:-",division(num1,num2))
    elif "//"==operation:
        print("floorDivision:-",floorDivision(num1,num2))
    elif "%"==operation:
        print("Modulus:-",modulus(num1,num2))
    elif "**"==operation:
        print("Exponential:-",exponential(num1,num2))
    else:
        print("Invalid Operation")
    choose=input("Do you want to perform yes/no:-").upper()
    if choose=="NO":
        print("Exit Successfully")
        break
'''
# using class,if-elif-else,while loop
'''class calculator:
    def getNumber(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def addition(self):
        return self.number1+self.number2
    def subtraction(self):
        return self.number1-self.number2
    def multiplication(self):
        return self.number1*self.number2
    def division(self):
        return self.number1/self.number2
    def floorDivision(self):
        return self.number1//self.number2
    def modulus(self):
        return self.number1%self.number2
    def exponential(self):
        return self.number1**self.number2
operation=calculator()
while True:
    num1=float(input("Enter first number is:-"))
    num2=float(input("Enter the second number is:-"))
    operations=input("choose_operation(+,-,*,/,//,%,**):-")
    operation.getNumber(num1,num2)
    if operations=="+":
        print("Addition:-",operation.addition())
    elif operations=="-":
        print("Subtraction:-",operation.subtraction())
    elif operations=="*":
        print("Multiplication:-",operation.multiplication())
    elif operations=="/":
        print("Division",operation.division())
    elif operations=="//":
        print("Floor_Division:-",operation.floorDivision())
    elif operations=="%":
        print("Modulus:-",operation.modulus())
    elif operations=="**":
        print("Exponential:-",operation.exponential())
    else:
        print("Invalid Operation")
    choose=input("Do you want to perfrom Yes/No:-").lower()
    if choose=="no":
        print("Exit Successfully")
        break'''

# using function,match-case,while loop
def addition(number1,number2):
    return number1+number2
def subtraction(number1,number2):
    return number1-number2
def multiplication(number1,number2):
    return number1*number2
def division(number1,number2):
    return number1/number2
def floorDivision(number1,number2):
    return number1//number2
def modulus(number1,number2):
    return number1%number2
def exponential(number1,number2):
    return number1**number2
while True:
    num1=float(input("Enter a First Number is:-"))
    num2=float(input("Enter a Second Number is:-"))
    operation=input("choose your operation(+,-,*,/,//,%,**)")
    match operation:
        case "+":
            print('Addition:-',addition(num1,num2))
        case "-":
            print("Subtraction:-",subtraction(num1,num2))
        case "*":
            print("Multiplication:-",multiplication(num1,num2))
        case "/":
            print("Division:-",division(num1,num2))
        case "//":
            print("floor_Division",floorDivision(num1,num2))
        case "%":
            print("Modulus:-",modulus(num1,num2))
        case "**":
            print("Exponential:-",exponential(num1,num2))
        case _:
            print("Invalid Operation")
    choose=input("Do you Want to do perform Yes/No:-").lower()
    match choose:
        case "no":
            print("Exit Sucessfully")
            break

                