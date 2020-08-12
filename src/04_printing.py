"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"   #NOTE ABOUT THIS =  %d will truncate to integer, %s will maintain formatting, %f will print as float and %g is used for generic number
print("x is %d, y is %g, z is \"%s\"" % (x,round(y,2),z) , "USING THE % OPERATOR") # You can do this like this as well = 

# Use the 'format' string method to print the same thing
#print("x is"+" " + str(x) +", " + "y is" +" "+ str(round(y,2)) +", "+"z is"+ " "+ str(z) , "Using format string")
print ("x is {}, y is {:.2f}, z is \"{}\"".format(x,y,z), "using the .format string")

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {round(y,2)}, z is \"{z}\" " , "USING THE F STRING")