# WAP in 'py' to print 1 to 10 odd no. using while loop
print("<------------------------using while loop---------------------------->")
a=1
while a<=10:
    if a%2!=0:
        print(a)
    a+=1

# WAP in 'py' to print 1 to 10 odd no. using for loop
print("<------------------------using for loop first way---------------------------->")
for i in range(1,11,2):
    print(i)
print("<------------------------using for loop second way---------------------------->")
for i in range(1,11):
    if i%2!=0:
        print(i)
    i+=1

