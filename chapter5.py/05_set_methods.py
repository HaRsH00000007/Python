#Creating an empty set.
b=set()
print(type(b))
print(b)


#Adding values to an empty set
b.add(2000)
b.add(2000)     # ---> Adding a value repeatedly does not changes a set.
b.add(2305)
b.add((1,5,4))
#b.add([2,8,5]) # ---> We can't add list to a set because list is mutuable or unhashable.
#b.add({1:6})   # ---> We can't add dictionary to a set because dictionary is also mutuable or unhashable.
print(b)


# Length of the set.
print(len(b))   # ---> Prints the length of this set.


# Removal of an element.
b.remove(2000)  # ---> Removes 2000 from set 'b'
#b.remove(6500)  # ---> Returns an error while trying to remove 6500(which is not present in the set).
print(b)

print(b.pop())
print(b)

