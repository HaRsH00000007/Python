from msilib import type_long


MyDict={
    "Streamer" : "Harsh wants to play a lot of games online",
    "Gamer" : "I will play when i will be tension free ",
    "Harsh": "I wanna know what is life",
    "Life" : "I wanna enjoy this life ,But when God",
    "Marks" : [20, 25, 65,],
    "Anotherdict" : {'Harsh':'Cookie'},
    2:36000
    }

#Dictionary Methods
print(type(MyDict.keys()))  #  --->   Prints the type of dictionary.
print(list(MyDict.keys()))  #  --->   Prints the keys of the dictionary in list form.
print(list(MyDict.values()))#  --->   Prints the values of the dictionary in list form.
print(MyDict.items())       #  --->   Prints the (key,value) for all contents of the dictionary.
print(MyDict)
updateDict={
    "Rohan"  :"Friend",
    "Shivani":"Friend"
}
MyDict.update(updateDict)   #   --->  Updates the dictionary by adding key value pairs from (updateDict)
print(MyDict)

print(MyDict.get('Rohan'))  #   --->  Prints value associated with key 'Rohan'
print(MyDict['Rohan'])      #   --->  Prints value associated with key 'Rohan'

#The Difference between .get and [] syntax in Dictionaries.
print(MyDict.get('Rohandi')) #   ---> Returns 'None' as 'Rohandi' is not present in dictionary.
print(MyDict['Rohandi'])     #   ---> Throws an 'Error' as 'Rohandi' is not present in dictionary.

  