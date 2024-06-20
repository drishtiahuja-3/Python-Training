def add(num1, num2, num3):
    result = num1 + num2 + num3
    print("result is :{}".format(result))

#function overloading 
add(10, 20, 30)
add(num1 = 10, num2 = 20, num3 = 30)
# default arguments / inputs 
def square(num = 5):
    num *= num
    print("square is :", num)
square()
square(3)


# to give default values in function give it in the right 
"""def add(num1 = 10, num2)
error """
def subtract(num1, num2 = 10):
    result = num1 - num2 
    print("result is :{}".format(result))
subtract(5)

