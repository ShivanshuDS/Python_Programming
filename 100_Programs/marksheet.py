# wap of marksheet. find out its total,its percentage and division. Enter the six subject marks.
english=int(input("Enter a English marks:-"))
hindi=int(input("Enter a hindi marks:-"))
math=int(input("Enter a math marks:-"))
science=int(input("Enter a Science marks:-"))
Pd=int(input("Enter a Physical Education marks:-"))
Total=english+hindi+math+science+Pd
print("Toatal marks of 6 subject:-",Total)
percentage=Total/6
print("Total Percentage:-",percentage)
if percentage>=90 and percentage<=100:
    print("First Division")
elif percentage>=70 and percentage<90:
    print('Second Division')
elif percentage>=40 and percentage<70:
    print('Third Division')
else:
    print('Fail')