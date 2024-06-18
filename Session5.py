# loop revision(ELEVATOR PROBLEM)
floors = 10 
floor = 0 # 0 or default floor 

floor_to_go = int(input("Enter the floor Number to go : "))
"""
while floor <= floors: #0 <=10
    print("At floor number:" , floor)
    
    
    if floor_to_go == floor:
        print("You have raeched at", floor_to_go)
        break
    
    floor += 1
"""

# FOR loop 
for floor in range(0, 11):
    print("At floor number:" , floor)
   
    if floor_to_go == floor:
        print("You have raeched at", floor_to_go)
        break


    