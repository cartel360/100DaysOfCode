year = int(input("Enter Year: "))

if ((year % 4 == 0 and year % 100 == 0) or year % 400 == 0):
    print(year, "is Leap Year")

else:
    print(year, "is not Leap Year")
