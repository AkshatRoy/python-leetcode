year = int(input("Enter year : "))

if year%100==0:
    print("Leap year" if (year%400 == 0 ) else "Not a leap year")

else:
    print("Leap year" if (year%4== 0) else "Not a leap year")