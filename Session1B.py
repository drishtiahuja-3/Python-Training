#Multi Value Container 
friends = ("john", "jennie", "jim", "jack", "joe")
print(friends, id(friends), type(friends))
#homogeneous 

friends = ("john", "jennie", "jim", "jack", 1002)
print(friends, id(friends), type(friends))
#heterogeneous

print(friends[0], id(friends[0]), type(friends[0]))
print(friends[1], id(friends[1]), type(friends[1]))
print(friends[2], id(friends[2]), type(friends[2]))
print(friends[3], id(friends[3]), type(friends[3]))
print(friends[4], id(friends[4]), type(friends[4]))


#tuple cannot be changed once created immutable

#modify
# error  
#friends[0]= "johnathon"

#mvc-list
friends = ["john", "jennie", "jim", "jack", 1002]
print(friends, id(friends), type(friends))

print(friends[0], id(friends[0]), type(friends[0]))
print(friends[1], id(friends[1]), type(friends[1]))
print(friends[2], id(friends[2]), type(friends[2]))
print(friends[3], id(friends[3]), type(friends[3]))
print(friends[4], id(friends[4]), type(friends[4]))
#list can be changed once created immutable

#modify
friends[0]= "johnathon"
print(friends[0], id(friends[0]), type(friends[0]))
print(friends[1], id(friends[1]), type(friends[1]))
print(friends[2], id(friends[2]), type(friends[2]))
print(friends[3], id(friends[3]), type(friends[3]))
print(friends[4], id(friends[4]), type(friends[4]))