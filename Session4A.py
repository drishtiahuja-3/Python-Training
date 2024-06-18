instagram_user_names = ["john.j", "fionna", "harry_h", "leo.32","ben_a"]
names = ["john jackson", "fionna flynn", "harrison", "leonardo", "bennethan"]
 
user_name = input("Enter user name to search:")
idx = 0
"""
if user_name == instagram_user_names[idx]:
    print("Name is:", name[idx])
elif user_name == instagram_user_names[idx+1]:
    print("Name is:", name[idx+1])
elif user_name == instagram_user_names[idx+2]:
    print("Name is:", name[idx+2])
elif user_name == instagram_user_names[idx+3]:
    print("Name is:", name[idx+3])
elif user_name == instagram_user_names[idx+4]:
    print("Name is:", name[idx+4])

else: 
    print("not found..")
"""
# not  a perfect approach
"""
## while loop
#linear search 
while idx < len(instagram_user_names):
    if user_name == instagram_user_names[idx]:
        print("Name is:", names[idx])
        break
    else:
        print("not found ")
        break
    idx +=1
"""

### or 
flag = False 
while idx < len(instagram_user_names):
    if user_name == instagram_user_names[idx]:
        print("Name is:", names[idx])
        flag = True 
        break
    idx +=1
if flag == False:
    print("username", user_name, "not found...") 


"""
##for loop 
for idx in range(0,len(instagram_user_names)):
    if user_name == instagram_user_names[idx]:
        print("Name is:", names[idx])
"""
