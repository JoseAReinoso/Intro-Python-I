# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)



# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(number):
    if (num % 2) == 0:
        return "number is Even"

    else:
        return "number is Odd"

print(is_even(num))


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if (num % 2) == 0:
    print("Even")

else:
    print("Odd")


 
