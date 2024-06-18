print("hello world")
question 1:
def hello_name(user_name):
print(f"hello_{use_name}!)
This function takes a user_name as input and prints a greeting message in the
 format "hello_username!".The f-string formatting is used to insert
  the user_name into the string.

  quetion 2:
  Here is the python function first_odds that prints the odd number from 1 to 100 and return nothing:
  def first_odds():for in range(1,101):if i %2!=0: print(I)
  Here is explanation of the code:
  The function
  first_odds
  take no argument and return nothing.
  The for loop iterates from to 100(inclusive) using the range function.
  For each number i in the loop,we check if it is and odd number by using the modulo operator(%).
  if i divided by 2 leaves a remainder of 1( i % 2! = 0), then its is an odd number.
  if i is an odd number we print it using the print function.
  call the function first_odds() to run the code and print the odd numbers from 1 to 100.
  Example output: 
  1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75
  77 79 81 83 85 87 89 91 93 95 97 99.
  
Question 3:
Here is a Python function named max_num_in_list that returns the maximum number from a given list:

def max_num_in_list(a_list): return max(a_list)
Here's a breakdown of what the code does:

The function takes a single argument a_list,which is the input list of numbers.
The max function is used to find the maximum value in the list.
The return statement sends the maximum value back to the caller.
You can test the function with a sample list, like this:

my_list = [3, 1, 4, 2, 5] result = max_num_in_list(my_list) print(result) # Output: 5

Question 4:
Here is the Python function that determines if a given year is a leap year:

def is_leap_year(a_year): if a_year % 4 == 0: if a_year % 100 == 0: if a_year % 400 == 0: return True else: return False else: return True else: return False

If the year is not divisible by 4, it's not a leap year, so return
False.
If the year is divisible by 4, it might be a leap year. Check if it's also divisible by 100.
If the year is divisible by 100, it's not a leap year unless it's also divisible by 400.
If the year is divisible by 400, it's a leap year!


Question 5 :
Here is a Python function that checks if all numbers in a list are consecutive numbers:

def is_consecutive(a_list): if len(a_list) < 2: return True a_list.sort() return a_list == list(range(a_list[0], a_list[-1] + 1))

First, we check if the length of the list is less than 2. If it is, we return True immediately, because a list with only 1 element or 0 elements is considered consecutive.
We sort the list to put the elements in ascending order. We then check if the sorted list is equal to a list of consecutive numbers from the smallest to the largest element in the original list. We do this using the
range function, which generates a sequence of numbers starting from the smallest element (a_list[0]) to the largest element
 (a_list[-1] + 1). We convert this range to a list using the list function.
If the sorted list is equal to the list of consecutive numbers, we return True. Otherwise, we return False.

Here are some examples:

>>> is_consecutive([2, 3, 4, 5, 6, 7]) True >>> is_consecutive([1, 2, 4, 5]) False >>> is_consecutive([1]) True >>> is_consecutive([]) True >>> is_consecutive([1, 3]) False



