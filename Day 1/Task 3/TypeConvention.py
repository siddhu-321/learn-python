#       Type Conversion in Python

# 1. int() → converts a value into an integer

x = int("10")      # string to int
print(x, type(x))  
# Output: 10 <class 'int'>

y = int(3.9)       # float to int (decimal part removed)
print(y)  
# Output: 3

# 2. float() → converts a value into a floating-point number

a = float("7.5")   # string to float
print(a, type(a))  
# Output: 7.5 <class 'float'>

b = float(5)       # int to float
print(b)  
# Output: 5.0

# 3. str() → converts a value into a string

p = str(100)       # int to string
print(p, type(p))  
# Output: 100 <class 'str'>

q = str(3.14)      # float to string
print(q, type(q))  
# Output: 3.14 <class 'str'>


# Exercise 

# 1. Ask the user for an integer, then convert it into float and print it.
User = 45
# Convert into float
convert = float(User)
print("User Ask : ",User," Convert into float Value : ",convert,sep=' ',end='\n')

# Practice Exercises (Type Conversion)

# Ask the user for an integer, then convert it into float and print it.

# Ask the user for a decimal number, convert it into int, and print it.

# Take a number input, add 5 to it (make sure it’s an int first), and print the result.

# Convert an integer into a string and concatenate it with another string.

# Example: age = 20 → "I am 20 years old"

# Convert the string "123.45" into both float and int and print both results.