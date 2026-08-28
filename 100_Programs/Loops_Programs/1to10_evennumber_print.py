# WAP in 'py' to print 1 to 10 even numbers using while loops

print("<----------------using while loop------------------------------------>")
a=1
while a<=10:
    if a%2==0:
        print(a)
    a+=1

print("<----------------using for loop------------------------------------>")
# using for loop
for  i in range(1,11):
    if i%2==0:
        print(i)