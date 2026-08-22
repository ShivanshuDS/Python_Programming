age=int(input("Enter your age:-"))
if age>0 and age<18:
    print("you are not eligible for vote")
elif age>=18 and age<150:
    print('you are eligible for vote')
else:
    print("invalid age")

# enter the age of person and find out the child, young and old.
if age>0 and age<18:
    print("you are child")
elif age>=18  and age<=35:
    print("you are young")
elif age>35 and age<150:
    print("you are old")
else:
    print('invalid age')