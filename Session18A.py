def add(num1, num2):
    sum = num1 + num2
    return sum

compute = add

def compute(num1, num2):
    return num1 + num2 *2
square = compute

result1 = square(10,2)
print(result1)
reslut2 = add(10,2)
print(reslut2)

# when we need to pass variable input to function 
#args arguments(tuple) kwargs key word arguments(dict)
def add(*args):
    print(args)
    data = list(args)
    print(data)
    print(type(args))
    print(type(data))

add(10, 20, 30 ,"hello", "john")
print("================================================")


def num(**kwargs):
    print(kwargs)
    print(type(kwargs))

num(a=10, b=20, c=30)

def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(10, 20, 30 ,"hello", "john",a=10, b=20, c=30)