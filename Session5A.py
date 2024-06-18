"""
for i in range(0,3):
    print(" \ni is :", i)

    for j in range(0,5):
        #print("j is :", j)
        print(j, end = " ")
"""
# chess board 
"""
0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
"""
white = "\u25A0"
black = "\u25A1"
"""
for i in range(0,8):
    #print("\n")
    for j in range(0,8):
        if i % 2 ==0:
            print(j%2, end =" ")
        else:
            print((j+1)%2 , end = " ")
    print()
"""
"""
for i in range(0,8):
    #print("\n")
    for j in range(0,8):
        if i % 2 ==0:
            if j%2 == 0:
             print(black , end =" ")     
            else:
              print(white , end = " ")  
        else:
            if (j + 1)% 2 == 0:
               print(black , end =" ")     
            else:
              print(white , end = " ")
    print()
"""

# hw place king and queen on their right position
# place knights 
for i in range ( 0 , 8):
    for j in range ( 0 , 8):

        if i == 0 :
            if j == 3:
                print('\u265B' , end = " ")
            elif j == 4:
                print('\u265A' , end = " ")
            elif j == 1 or j == 6:
                print('\u265E' , end = " ")
            elif j == 0 or j == 7:
                print('\u265C' , end = " ")
            elif j == 2 or j == 5:
                print('\u265D' , end = " ")
            else:
                if j%2 == 0:
                    print('\u25A0' , end = " ")
                else:
                    print('\u25A1' , end = " ")


        elif i == 7:
            if j == 3:
                print('\u2655' , end = " ")
            elif j == 4:
                print('\u2654' , end = " ")
            elif j == 1 or j == 6:
                print('\u2658' , end = " ")
            elif j == 0 or j == 7:
                print('\u2656' , end = " ")
            elif j == 2 or j == 5:
                print('\u2657' , end = " ")
            else:
                if j%2 == 0:
                    print('\u25A0' , end = " ")
                else:
                    print('\u25A1' , end = " ")

        elif i == 1 :
            print('\u265F' , end = " ")

        elif i == 6:
            print('\u2659' , end = " ")            
        
        else:
            if(i%2 == 0):
                if j%2 == 0:
                    print('\u25A0' , end = " ")
                else:
                    print('\u25A1' , end = " ")

            else:
                if (j+1)%2 == 0:
                    print('\u25A0' , end = " ")
                else:
                    print('\u25A1' , end = " ")
    print()
    
