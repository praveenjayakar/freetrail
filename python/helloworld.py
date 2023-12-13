#!/bin/python
'''
print("Hello world")

name = "jhon"
age = 25
height = 5.5
is_student = False

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student?", is_student)

'''
'''
#list

fruits = [ "apple" , "banana" , "kiwi" ]
print("Number of Fruits: " , len(fruits))

print("First Fruit: ", fruits[0])

print("All fruits: " , fruits )

fruits.append("orange")

print("After appending fruit list: " , fruits )

fruits[1] = "kiwi"

fruits.remove("apple")

print(fruits)
'''

'''
#Dictionaries

person = { "name" : "Praveen" , "age" : 27 , "city" : "Palasa" }

print(person)

print("His name: " , person["name"])

print("His age: " , person["age"])

person["occupatiom"] = "Engineer" 

person["age"] = 30

print('after adding occ and updated age :' , person )

del person["city"]

print(person)

#loops

for key , value in person.items():
    print(key + ":" , value)

for value in person.items():
        print("key" + ":" , value)
'''


def greet(name):
    #this function greets user 
    print("Hello, " + name + "!")
greet("praveen")

greet("Elon")


for i in "rakesh" , "shyam" , "moyo" :
    greet(i)


