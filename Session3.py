#Controller
"""1. operators
2. conditional constructs(if/else)
3. iterations/loops"""

#OPERATORS 
#ARITHMETIC (+,-,*, **, /, //, %)
product_price = 200
gst_tax = 0.18
price_to_pay = product_price + gst_tax*product_price
print(price_to_pay, id(price_to_pay), type(price_to_pay))


number =10 
result = number/3
#result = number // 3 
print("result is :", result)

base = 2
result = base * 2
#result = base ** 3
print("result is :", result)

bucket_size = 7
hashcode = 120 % bucket_size
print("hashcode is :", hashcode)


#ASSIGNMENT operator(=, +=, -=, *=, **=, /=, //=, %=)
# a new reference variable age, will be created in stack
# aq container 20 will be created in heap 
# hashcode of 20 will be stored in age 
age = 20 
#update operation 
#age = age + 10 
age += 10 #Shorthand operator add and asign 
print("age is ", age)
age %= 3
age -= 1
print("age is ", age)





#increment and decrement 
qty = 1 
qty += 1
qty -= 1
qty += 5
qty -= 1
qty **= 2
print ("qty is :", qty) #25 


