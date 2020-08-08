# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
newx = x.append(4)
print(x, "-with the 4 added")

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
newxWy= x + y

print(newxWy, "-y values added to x list")

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
y.pop(0) # this is removing the first element of y
newY = x + y
print(newY, "-this is removing the first y element and appending it to x")

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
newY.insert(5,99) # this is inserting the 99 on the 5th place in the list
print(newY, "-With 99 added on the fift place in the list, right before the 10")

# Print the length of list x
# YOUR CODE HERE



# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
    print(i * 1000)