def binarySearch(arr, l, r, x):

    if r >= l:
 
        mid = l + (r - l) // 2
 
        if arr[mid] == x:
            return mid
 

        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        return -1
 

n = int(input("Enter the no. of elements : "))
lst = []
for i in range(n):
    lst.append(int(input()))
x=int(input("Enter element you want to search: "))
result = binarySearch(lst, 0, len(lst)-1, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")