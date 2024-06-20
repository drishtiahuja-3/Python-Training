""" 
functions 
relationship mapping between objects 
"""
def add(num1, num2):
    result1 = num1 + num2
    print("result is :{}".format(result1))

print("add is :", add)
print(hex(id(add)))
add(10, 20)

#reference copy operation
hello = add
hello(11,22)

def add(num1, num2, num3):
    result = num1 + num2 +num3 + 10
    print("result is :{}".format(result))

print("add is :", add)# have different hash code bcoz of memory optimization
print(hex(id(add)))
add(10, 20 , 30)