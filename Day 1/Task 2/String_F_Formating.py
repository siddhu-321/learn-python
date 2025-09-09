#    String F Formatting 

#  Python have 3 main format of String 
# 1. f-String 
# 2. .format() method
#  3. % formatting (Old Style)

#                           f- String Formatting

name = "Siddharht"
age  = 34
height = 5.754

#  Basic Expression 
print(f"My name is {name}, I am {age} Years Old")

#  Expression
print(f"In 5 Years, i will be {age+ 5} Year Olds")

#  Formating Number

print(f"my height is {height: .1f} now")

print("---------------------------------------------------------------------------------------------------------")

# 2. Format Method
name2 = "Sakshi"
age2 = 22
height  = 5.4567

# Basic expression 
print("She is name of {}".format(name2))

# Postional Expression
print("she is name of {0}, she is {1} now".format(name2, age2))

# Named Argument 
print("she i height now is {h:.2f}".format(h=height))


print("-------------------------------------------------------------------------------------------------------------")

#  Old Style Formatting 

e1 = "Neelam"
e2 = 52
heigt= 5.45444

print("My name is %s, I am %d Years old"%(e1,e2))

print("she is height of %.2f"%heigt)
