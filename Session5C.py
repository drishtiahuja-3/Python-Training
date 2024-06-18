# memory representation of function 

def square(num):
    print(" num is:", num , id(num))
    num *= num
    print(" num is:", num , id(num))
    return #termination statement

# print("square is :", square ) function exist in memory 
#rest is the property of main function 
# 1- 4 is the property of square function

number = 10
print(" Number is :", number, id(number))
square(number)
print(" Number is :", number, id(number))
