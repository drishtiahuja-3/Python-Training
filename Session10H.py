#BUBBLE SORT

def sort(lst):
    n = len(lst)
    for i in range(n):
     
        for idx in range(n-i-1):
            if lst[idx] > lst[idx+1]:
                temp = lst[idx]
                lst[idx] = lst[idx + 1]
                lst[idx + 1] = temp
    




n = int(input("Enter the number of elements to be sorted: "))
lst =[]
print("Enter the elements to be sorted: ")
for i in range(n):
    ele = int(input())
    lst.append(ele)

print("\n\n--------------------------SORTING--------------------------------------\n")
print("\t\tBefore Sorting:", lst)
print("\t*****************************************************")
sort(lst)
print("\t\tAfter sorting: ", lst)
print("\n-------------------------------------------------------------------------")