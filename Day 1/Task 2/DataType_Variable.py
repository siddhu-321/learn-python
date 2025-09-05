#               DataType Variable And Name Convention

#   What is Variable 
#     Variable is like  a Containier , that hold date. Creating a Variable like Creating a placeholder on a memory and assigning it same value. In Python it is easy as writing 

a=1
b= True
c="siddharth"
d=None
print(a," ",b," ",c," ",d)

# DataType  :- Datatype in python is a specify that type of value a varable hold. this is required in programming to do various operation without causing an error

# Numeric Datatype : Int , Float, Complex

# int → Integer numbers (poore number, bina decimal ke)
a=123
print("Value type : -", type(a))

# float → Decimal / floating-point numbers

b= 1.6
print("VAlue type :-", type(b))

# complex → Complex numbers (a + bj form me)

c = 5_8j
print("VAlue type :-", type(c))

# Text DataType : str 

#   str → String (text data, quotes me)
d = "Siddharth"
print("VAlue type :-", type(d))

#  Boolean DatType :- It consists of value True & False
e = True
print("VAlue type :-", type(e))


#  Sequence Type DataType :  1. List , 2. tuple , 3. Range 

#   1. List : - Ordered, mutable (changeable), allows duplicates
#           a List is and Ordered Collection of Data with elements separated by a comma and enclosed within sequare brackets. List are Multiple and can be Modified After Creation

f = [1,2,3,4,5]
print("VAlue type :-", type(f))
lIst1 = [1,2,[34,43,53],["Hello","King"]]
print("Value of Type :- ", type(lIst1),"Printed as  ", lIst1)

#   2. Tuple  ;- Ordered, immutable (not changeable), allows duplicates
#               A Tuple is an ordered Collection of data with elements Separated by a comma and enclosed within parathensis. Tuple are immutable and can not be modified after creation

my_tuple = (1, 2, 3, "apple")  # tuple
print("Value of Type :- ", type(my_tuple),"Printed as  ", my_tuple)



#   3. range :-  Sequence of numbers (mostly loops ke liye use hota hai)

r = range(5)   # 0,1,2,3,4
print("Value of Type :- ", type(r),"Printed as  ", r)


#  Set Types   :-   

# set → Unordered, no duplicates

my_set = {1, 2, 3, 3}   # {1, 2, 3}
print("Value of Type :- ", type(my_set),"Printed as  ", my_set)

# frozenset → Immutable set

f_set = frozenset([1, 2, 3])
print("Value of Type :- ", type(f_set),"Printed as  ", f_set)


#  Binery Type :-

#  bytes, bytearray, memoryview → Mostly low-level data handling ke liye
b = b"Hello"             # bytes
ba = bytearray(5)        # bytearray
mv = memoryview(b"abc")  # memoryview

print("Value of Type :- ", type(mv),"Printed as  ", mv)

