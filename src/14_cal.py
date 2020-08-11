"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

1. Write a program that accepts user input of the form
  `14_cal.py [month] [year]`  # USE =  args = sys.argv
and does the following:
2. - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
3. - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
4. - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
5. - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#1
args = [int(n) for n in  sys.argv[1:]] # this is used to pass arguments to a program, to execute it would be python 14_cal.py argument argument.
#example in this case if you want to pass 4 and 2021  you do python 14_cal.py 4 2021
print(args, len(args))

#2
if len(args) == 0:
  #no input from the user inserted
  month = datetime.now().month
  year = datetime.now().year
#3  
elif len(args) == 1:
  month =args[0]
  year = datetime.now().year
#4  
elif len(args) == 2:
  month = args[0]
  year = args [1]
#5  
else:
  input("please provide a month and year int the following format xx xxxx")


print(month, year) 

