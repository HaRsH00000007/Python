# Write a program to find out whether a student is pass or fail, if it requires total 40% and atleast 33% in each subject to pass.
# Assume 3 subjects and take marks as an input by the user.
Sub1=int(input("Enter marks of 1st subject\n"))
Sub2=int(input("Enter marks of 2nd subject\n"))
Sub3=int(input("Enter marks of 3rd subject\n"))

if (Sub1<33 or Sub2<33 or Sub3<33):
    print("You failed because you have scored less than 33 in one of the subjects")
elif(Sub1+Sub2+Sub3)/3 <40:
    print("You failed because you have scored less then 40 while considering overall subjects Marks")
else:
    print(" Congratulations, You Made It Buddy ")

