# write a program and input a year and find out it is leap year.
# year, year/4==0:
year=int(input("Enter a Year:-"))
if year%4==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")