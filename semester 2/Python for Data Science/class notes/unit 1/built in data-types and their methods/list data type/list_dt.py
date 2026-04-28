#List are similar to array found in other languages
#They are ordered and mutable collection of items.
#It is very flexible as items in a list do not need to be of the same data type
#List can also be created using constructor list()

a = []
a = [1,2,3] # Will get overwritten on the above of the same array named 'a'
print(a)

b = ["Geeks","for","Geeks",4,5]
print(b)

a = list((4,5,6,'apple',4.5))
print((a))

b = list("GFG")
print(b)

#Creating list with repeated elements
a = [2]*5
b = [0]*7

print(a)
print(b)