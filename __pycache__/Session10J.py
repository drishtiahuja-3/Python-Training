def sort(lst):
    for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
                 
            while j >= 0 and key < lst[j]:
                lst[j + 1] = lst[j]
                j = j - 1
        
            lst[j + 1] = key

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