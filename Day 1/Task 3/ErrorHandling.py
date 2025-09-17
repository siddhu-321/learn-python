    #               Input Handling And Error Handling  Exception handling

#  Exception Handling is the Process of Responding to unwanted or unexpected events when  a computer program run. Exception handling deals with these events to avoid the program or system crashing and without this price exception would disrupt the normal operation of a program

# Python has many built in exception that are raised when the program encounters an error (Something in the program goes wrong)
# when these Exception occus the python intrepretor stop the current process and pass it to the calling process until it is handled if not handled the program will crash

num = input("First Number : ")
num1 = input("Second Number : ")

try:
    print(int(num))
except ValueError as e:
    print(e)