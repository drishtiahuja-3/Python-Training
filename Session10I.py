#selection sort 
def sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1 , n):
            if lst[j] < lst[min_idx]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i] 

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




