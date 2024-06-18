"""
def print_num(number):
    print(number)
    if number < 10:
        print_num(number + 1)

print_num(1)

#func calling itself again and again
 
"""

 # Factorial of a number using recursion

def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

num = int(input("enter the number to find factorial: "))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", fact(num))
