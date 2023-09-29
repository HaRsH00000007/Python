#Write a programme to create a dictionary of hindi words with values as their english translation. Provide user with an option to look it up.
myDict={
    "Pankha":"Fan",
    "Kursi":"Chair",
    "Hawa" :"Air",
    "Paani":"Water",
    "Khushi":"Harsh"
}
print("options are",myDict.keys())
a=input("Enter the hindi word\n")


#print("The meaning of your word is:", myDict[a])


#Below line will not return an error if the key is not present in the dictionary because of ".get" function.
print("The meaning of your word is:", myDict.get(a))
