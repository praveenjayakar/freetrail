#!/bin/python3

x = [ "x","y","z"]
y = ( "x","y","z")

print(type(x))
print(type(y))

print(x[1])
print(len(y))

x.insert(0, "w")

w=list(y)
w.append("k")

print(w)

H = [ 23 , 66 , 65 , 77, 11 , 100 ]

print(H)

U = sorted(H)

print(U)


numbers = [200, 40, 160, 80, 1000]
numbers.sort()
print(numbers)
