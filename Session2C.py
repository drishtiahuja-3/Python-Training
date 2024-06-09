#input output operation in python

name = input("Enter your name:  ")
print("name is:", name)
print("type of name is:", type(name))
print("hash_code of name is:", id(name))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 

#this takes age in string by default
age = input("Enter your age:  ")
print("age is:", age)
print("type of age is:", type(age))
print("hash_code of age is:", id(age))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 

#to take integer inputs in age 
age = int(input("Enter your age:  "))
print("age is:", age)
print("type of age is:", type(age))
print("hash_code of age is:", id(age))