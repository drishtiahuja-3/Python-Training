#mvc function in memory 
def square(num):
    print(" num is:", num , id(num))
    for i in range(0, len(num)):
        num[i] *= num[i]
    print(" num is:", num , id(num))
    return 

    
number = [10, 20, 30, 40 ,50]
print(" Number is :", number, id(number))

square(number)
print(" Number is :", number, id(number))
# hash code will be same of mvc