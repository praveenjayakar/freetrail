#!/bin/python3


mytuple = ("Ant", "Banana" , 5, 10, 15, 0.6, "Karthik")

print(mytuple[0])

length=len(mytuple)

print(length)

def get_coordinates():
    return (3,4)

x , y = get_coordinates()

print(x , y )

A = [ 5, 6, 7, 8, "ant" ]

for item in A:
    print(item)

print("-----------------tuple loop----------")

for item in mytuple:
    print(item)

for i in range(1,10):
    print(i)


servers = ['web-server-01', 'db-server-01', 'app-server-01']


print(servers)
print(servers[0])


