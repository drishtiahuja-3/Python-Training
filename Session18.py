"""
MULTI VALUE CONATINER
    SEQUENCES
        TUPLE
        LIST 
        STRING 
    SET 
    DICTIONARY 


    PROPERTIES 
    1. INDEXING
    2. NEGATIVE INDEXING
    3. SLICING 
    4. CONCATENATION 
    5. MULTIPLICITY 
    6. MEMBERSHIP TESTING 

"""

# 1d list 
""" indexing & negative indexing 
            0   1   2  
            -3  -2  -1 
"""
my_data = [10, 20, 30 ]

#2d lsit 
numbers = [
    [10, 20 , 30], #0
    [40, 50, 60],  #1
    [12, 11, 30]   #2
]

print(my_data[0])
print(my_data[-1])
print(len(my_data))

print(numbers[0])
print(numbers[-1])
print(len(numbers))

#3d list list of list of list 

large_data = [
    [
        [10, 20 , 30], #0
        [40, 50, 60],  #1
        [12, 11, 30]   #2
    ],

    [
        [10, 20 , 30], #0
        [40, 50, 60],  #1
        [12, 11, 30]   #2
    ]
]
print(large_data[1][0][0])

print(large_data[-1][-3][-3])

name = "john cafe"
name1 = """
john cafe menu
pizza 
burger
noodle 
"""
print(name1[2])

#RANGE FUNCTION 
data = list(range(10, 101, 10))
print("data is:")
print(data)

# SLICING 
print("data (0,3):", data[0:3])
print("data (3,7):", data[3:7])
print("data (5,...):", data[5:])
print("data (...,4):", data[:4])
print("data (0,-5):", data[:-5])
print("data (-5,-2):", data[-5:-2])


email = "john@example.com"
print("slicing:",email[-4:])
print("slicing:",email[12:])

#4. CONCATENATION 
data1 = [10, 20, 30]
data2 = [10, 20, 30]
data3 = data1 + data2 
print(data3)

#5. MULTIPLICITY 
data4 = data1 *2 
print(data4)

prices = [100, 500, 700, 300]
prices1 = prices * 2
prices = [100, 500, 700, 300]


#6. MEMBERSHIP TESTING 
print(10 in prices )
print(10 not in prices )
print(100 not in prices )


quote= "Search the candle rather than cursing the darkness"
print(quote[6])#blank space
print(quote.split(" "))


my_set = {10, 20, 30, 40, 50, 60}
# print(my_set[-1]) indexing & negative indexing doesnot work on sets
my_set2 = {80, 90}
# print(my_set + my_set2) concatenation doesnot work on sets
# print(my_set * 2) multiplicity doesnot work on sets
# slicing doesnot work on sets
print(10 in my_set)

student = { "rollno": 1,
"name":"john",
"age":20,
"address":"abc"}
print("student[age]", student["age"])
#print("student[age]", student["age":"address"])
print(1 in student) #MEMBERSHIPtesting only works for keys not values
print("name" in student)