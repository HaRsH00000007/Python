# Write a programme to find out whether given username is present in a list or not.
Names= [ "harsh", "shruti", "rohan", "bhutaani", "jaanvar", "pandit" ]
name= input("Enter name to check\n")
if name in Names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")