file =open("customer.csv", "r")
#data = file.read()
line = file.readlines()
print("file data:")
#print(data)
print(line)


for i in range(len(line)):
    print(line[i])
