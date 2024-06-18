""" 
another brick in wall 
who placed the last brick and how many ??
Mr. john: create a wall with 13 brick 
                bricks 
jack : 1        1
joe : 2         3

jack : 2        5
joe : 4         9

jack : 3        12
joe : 6         13

joe -> last brick 
    1 brick
"""
number = int(input("Enter the number of bricks to be used: "))
sum = 0
jack = 1 
joe = 2 * jack
while sum < number:
    sum += jack 
   
    if sum >= number:
        result = sum - jack 
        print("jack puts the last brick... i.e :", number - result )
        break
    else:
        print("jack put ", jack, "brick")

    sum += joe 
    
    if sum >= number:
        result = sum - joe 
        print("joe puts the last brick... i.e :", number - result )
        break
    else:
        print("joe put ", joe, "brick")

    jack = jack + 1
    joe = 2 * jack 