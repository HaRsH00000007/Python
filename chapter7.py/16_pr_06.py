# Write a programme to calculate the factorial of a given number using for loop.

num=int(input("Enter the number: \n"))
factorial= 1
for i in range( 1, num+1 ):
    factorial= factorial*i
print(f"The factorial of {num} is {factorial}")

