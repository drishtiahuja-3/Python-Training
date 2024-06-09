numbers = [10,20,30,40,50]
print(numbers, id(numbers), type(numbers))

#reference copy operation 
my_numbers  = numbers
print(my_numbers, id(my_numbers), type(my_numbers))


#update 
numbers[2]=1122
print(numbers[2])
print(my_numbers[2])
#same value 

#delete value
del numbers
print(my_numbers)