#  MAster of Input () Function and Print() Funtion

#  1. Print() Function 
#   USed to display output on the Screen

# Syntax
value1 = "sid"
value2 = 232
value3 = 5.3
print(value1, value2, value3, sep=' - ',  end='\n')

# Example 1
print("My","Name","is","Siddharth", sep='-',end='\n')


#   2. Input Method/Function    : -   Used to take input from the user.
variable = input("Message shown to user: ")
# Always returns a string, even if the user types a number.

#  Example 
name = input("Enter your name: ")
print("Hello,", name)
# Input: Alice
# Output: Hello, Alice

# Type Casting (because input() always returns a string)
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
# Input: 20
# Output: Next year you will be 21


pi = float(input("Enter value of pi: "))
print("Pi is approximately", pi)
# Input: 3.14
# Output: Pi is approximately 3.14



# 3. Practice Exercises

# Try these on your own 👇

# Ask the user for their name and print it.

# Ask the user for two numbers, add them, and print the sum.

# Take three words as input and print them in one line, separated by commas.

# Ask the user for a word and print it 5 times in a row.

# Print two lines, but use end=' ' so they appear on the same line.
