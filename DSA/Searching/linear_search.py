def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


n = int(input("Enter the no. of elements : "))
lst = []
for i in range(n):
    lst.append(int(input()))
x=int(input("Enter element you want to search: "))
result = linearSearch(lst, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)