lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))
sum = 0 
while (lower <= upper):
    sum = sum + lower
    lower+=1
print("Sum of numbers in the given range is : ", sum)