# def parrot(str='Squawk!'):
#     print(str)
#     return(str)
# print(parrot())
# In this lab, you'll be defining a function called parrot().

# The parrot() function should accept an argument of a string and both print() and return the string at the end of the function.

# The parrot() function should have a default argument of "Squawk!"

# NOTE: This lab is explicitly testing your ability to control the return value of a function: not just what it does, but what it returns.
# Remember, return values are important. What's the return value of print()?

def parrot(str='Squawk!'):
    print(str)
    return str
    # return str
x=parrot('string')
print(x)