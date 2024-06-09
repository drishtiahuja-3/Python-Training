numbers= {10,20,30,40,50,50}
print(numbers, id(numbers), type(numbers))
#set hashing 
#doesn't support duplicacy
#list tuple support duplicacy

john_friends = {"joe", "jim", "jack", "harry", "kim","joe"}
sia_friends = {"joe", "george", "fionna", "leo", "jack","ben"}

print(john_friends)
print(sia_friends)

mutual_friends = john_friends & sia_friends # intersection 
print(mutual_friends)
# print(john_friends[0]) #error
#set doesn't support indexing #it works on hashing
#hance we cannot get data from set