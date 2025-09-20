#Defining the rotate function
def rotate(first, second, third):
    return (third, first, second)

#Defining variables
a, b, c = 'Doug', 22, 1984

#First call
a, b, c = rotate(a, b, c)
print(a, b, c)

#Second call
a, b, c = rotate(a, b, c)
print(a, b, c)

#Third call
a, b, c = rotate(a, b, c)
print(a, b, c)
