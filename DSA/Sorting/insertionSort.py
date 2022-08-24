def insertionSort(arr,n):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Compare key with each element on the left of it until
        # an element smaller than it is found
        # --------------------------------------------------------
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        arr[j + 1] = key
    return arr
# Driver code to test above
n = int(input("Enter the no. of elements : "))
ipt = []
for i in range(n):
    ipt.append(int(input()))
print(insertionSort(ipt,n))
