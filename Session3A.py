#CONDITIONAL operators(==, !=, >, <, >=, <=)

cab_Fare = 500
e_wallet = 600 #200 false #500 false edge case boundary case
result = e_wallet > cab_Fare #e_wallet >= cab_Fare
print("Can i book the cab ",result) #true
print( type(result))

#LOGICAL (and , or)
email = input("enter email")
password = input("enter password")
print(" is login successful?")

result = (email == "john@example.com") and ( password == "john123")
print(result)

otp = 3027 
user_otp = int(input("enter otp"))
print("is otp correct ??", otp == user_otp)

#MEMBERSHIP TESTING (is, is not)
a =10 
b = 10 
print(a == b)#true
print(a is b)#true
print(a is not b)#false


#hw find difference bw == and is 




#BITWISE operators (&, |, ^)

num1 = 10 #1010 in binary 
num2 = 8 #1000 in binary 
print("num1 in binary is :", bin(num1))
print("num2 in binary is :", bin(num2))

result1 = num1 & num2  #and  1000 ->8
result2 = num1 | num2 #or    1010  ->10
result3 = num1 ^ num2 # xor  0010 ->2
print(result1) 
print(result2)
print(result3)


# interview imp 
# SHIFT Operator (>> right shift , << left shift )

num1 = 8 
num2 = 2 
result4 = num1 >> num2 #8//2^2
print(" right shift is :", result4)


num1 = 8 
num2 = 2 
result5 = num1 << num2 #8*2^2
print(" left shift is :", result5)

number = 11 
result6 = number >> 2
print(number, ">> 2 is ", result6)


# 11
# 0000 1011
# >> 2
# __00 0010 -> 2

# -11 
# 0000 1011 2s complement 
# 1111 0101
# >> 2
# __11 1101
# 1111 1101 2s complement 
# 0000 0011 -> -3

# 13 
# 0000 1101 
# >> 2
# __00 0011 -> 3

# -13 
# 0000 1101
# 1111 0011
# >> 2
# __11 1100
# 1111 1100
# 0000 0100 -> -4