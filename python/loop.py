
#for,while loops

fruits = [ "a", "b", "c", "d" ]

drinks = ( "x" , "y" , "z" )

for i in fruits:
    print(i)



count = 0
while count < 5:
    print(count)
    count += 1

num = 5
while num < 10:
    print(num)
    num += 1

print("----------------")

sum = 1

while sum%2 == 0:
    print(sum)
    sum += 3
    continue



print("----------")
number = [1,2,3,4,5,6,7,8,9]

for numbers in number :
    if numbers == 3:
        break
    print(numbers)




digits = [1,3,5,7,9,11,13,15,17,19,21]

for digit in digits:
    if digit == 11:
        continue
    print(digit)

    
