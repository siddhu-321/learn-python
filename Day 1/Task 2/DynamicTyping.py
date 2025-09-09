#           Dynamic Typing

# What do you mean Dynamic Typing

# Typing -> refer to datatype ( int , str, float so on.)
#  Dynamic -> mean decided at runtime ,  not fixed beforehand

# In Python you dont declare variable type explicitly
# the intrapreter figured out the type automatically when you  assign the value of variable.
# And Later you can even assign a completely different type to the same variable 

x= 10  # x is a int value
print(type(x))  #< class is int >

x = "Siddharth" # x is now String
print(type(x))  # < class is String>

x = 6.7 # x is now Float 
print(type(x))  # < class = float >


#  Pros of Dynamic  Typing 
#  1. Flexible & easy to write code
#   2.  Faster Prototyping (no need to declare type )

# Cons of  Dynamic Typing
#  1. Error my show up only runtime (Harder to catchup bugs)
#   2. can cause confusion if variable types keep changing