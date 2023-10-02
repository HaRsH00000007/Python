# Write a programme to find the sum of first "n" natural numbers using while loop.

num=int(input("Enter the number: \n"))
Sum= 0
while i in range( 0, num+1 ):
    Sum = Sum*i
print(f"The Sum of {num} is {Sum}")