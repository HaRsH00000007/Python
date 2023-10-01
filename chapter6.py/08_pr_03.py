# A spam comment is defined as a text containing following keywords. 
# "Make a lot of money" ,"Buy now", "Subscribe this", "Click this" . Write a program to detect these spams.
text=input("Enter the text\n")
if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("Subscribe this" in text):
    spam=True
else:
    spam=False


if(spam):
    print("This text is spam")
else:
    print("This text is not spam")