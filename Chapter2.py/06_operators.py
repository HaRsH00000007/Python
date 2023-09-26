#Aritbmetic Operators
from operator import truediv


a=5
b=6


print("the sum of 5+6 is",5+6)
print("the product of 5*6 is",5*6)
print("the difference of 5-6 is",5-6)
print("the division of 5/6 is",5/6)



#Assignment Operators
b=60
b+=5
b-=5
b*=10
b/=60
print(b)


#Comparison Operators
#c=(7==7)
#c=(7>19)
#c=(7<19)
#c=(7<=19)
#c=(7>=19)
c=(7!=19)
print(c)



#Logical Operators
crush1=True
crush2=False
print("The value of crush1 and crush2 is", (crush1 and crush2))  # "And" operator passes True when both crush1 and crush2 are true otherwise if anyone of them is false then "and" operator returns False. 
print("The value of crush1 or crush2 is",(crush1 or crush2))     # "Or" operator passes "True" if anyone , among crush1 and crush2 are "True". 
print("The value of not crush1 is",(not crush1))                 # "Not" operator always passes opposite of the given statement
