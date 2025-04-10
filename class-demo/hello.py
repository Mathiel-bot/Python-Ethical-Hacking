# This line is running python code without a variable
print("Hello World!")
print('I am learning python')


# Declaring a variable
First_name = "Oti"
Last_name = "Mathiel"

# Concatenation (concatenating the variables)
print(First_name + " " + Last_name)

"""
Types of variables
Integer- whole number (eg: 0-9)
floating-point (float) - Decimal numbers (eg: 0.1)
string(str) - Text Data ("hello", "Python" 'Text')
Boolean(bool) - True/false values
"""

age = 18
sentence = "The legal age to vote in"
country = "United Kingdom"

full_setence = sentence + " " + country

print(full_setence + " is " + str(age))


# List or Array
cars = {'BMW': 'X6', 'Mercedes': 'GLC300', 'Tesla': 'Model X', 'Audi': 'Q3'}
print(cars['BMW'])

Fruits = ['orange', 'banana', 'apple', 'pineapple', 'mango', 'grape']
print(Fruits[0])
print(Fruits[1])
print(Fruits[2])
print(Fruits[3])
print(Fruits[4])
print(Fruits[5])
print(Fruits[1:5])

# Builtin function to add item
Fruits.append('pear')

# #Remove an item
Fruits.remove('mango')
print(Fruits)

# Looping through an item multiple time using for statement
# identation works with control flow
for Fruits in Fruits:
     print(Fruits)

# Print an item in ranges
for i in range(5):
    print(Fruits)

# Looping through a line of code using while statement
count = 0
while count <= 10:
    print("count: " , + count)
    count += 2 # increment
    
  # Defining a function  
    def new_function(sum): # Parameter
        return sum
    
    print(4+4) # Value
    
    name = input("What is your name ")
    print("My name is " + name)
    
    change_ip = input("Type your IP addr: ")
    print("Your IP has been changed to " + change_ip)    