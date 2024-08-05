number = int(input("Enter a number : "))

print("===================WRONG================")

for check in range(2,number):
    if (check % number) == 0:
        print("Not a prime ")
        break
else:
    print("Prime number")


