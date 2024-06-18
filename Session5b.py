#function in memory
#main() function
# svc mvc in function 
# recursion in programming- using function in an iteration  
"""
print("HELLO ALL")
a = 10 
b = 20 
c = a + b
print("sum is :", c)
"""
# on main thread 5 different tasks are formed to execute these 5 instructions 
# print("__name__ is:", __name__) will have value as __main__
#MAIN FUNCTION 
def main():
    print("HELLO ALL")
    a = 10 
    b = 20 
    c = a + b
    print("sum is :", c)
#dunder- double underscore, it is a  magic variable defined in python which has its value as __main__
if __name__ =="__main__":
    main()

