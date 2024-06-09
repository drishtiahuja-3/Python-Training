#our very first program-->comment
#containers 

#single value container(svc)
#create statement -> creating a svc in RAM
user_name = "auribises"

#read statement -> to read data inside a container
print(user_name, id(user_name), type(user_name))

#update statement 
user_name = "Drishti"
print(user_name, id(user_name), type(user_name))
#id is a hash code 

#update statement 
user_name = 1002
print(user_name, id(user_name), type(user_name))

#delete statement 
del user_name
#from stack as well as heap
