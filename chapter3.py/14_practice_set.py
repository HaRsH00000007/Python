#Write a python programme to display a user entered name followed by Good Afternoon using input() function
Name=input("enter your name\n")
print("Happy Birthday"+Name)


#Write a programme to fill in a letter template given below with name and date:
Letter='''Dear <|Name|>, 
\t(^_^)  (^_^)  (^_^)  (^_^)  (^_^)
\tGreetings from Harsh's coding house.\n\tI am happy to wish my dearest Buddy Happy Birthday 
\tfrom my coding house in a unique way 
\tI hope the birthday cake is as sweet as you,
\tIt's not the years that count, it's the memories you make over these years
\tSo, Enjoy your life with positive vibes
\tAnd one more thing, I am blessed to have Buddy like you,
\tSo thanks a lot for always helping me
\tHave a great day ahead!
\tThanks and Regards\n\t(^_^) (^_^) (^_^) (^_^) (^_^)
\tDate:<|Date|>
'''
Name=input("Enter your Name/n")
Date=input("enter Date/n" )
Letter= Letter.replace("<|Name|>",Name)
Letter= Letter.replace("<|Date|>",Date)
print(Letter)


#Write a programme to detect double spaces in a string:
st="This is a string with  double  spaces"
doublespaces=st.find("  ")
print(doublespaces)



#Replace the double spaces from problem 3 with single spaces:
st="This is a string  with  double spaces"
st=st.replace("  "," ")
print(st)




#Write a programme to format the following letter using escape sequence characters:
letter="Dear Harsh , Your coding house is cool I like it"
print(letter)


formatted_letter="Dear Harsh ,\n\t Your coding house is cool\n I like it \nCOOLBOI"
print(formatted_letter)
