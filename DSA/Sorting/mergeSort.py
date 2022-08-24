def mergeSort(myList):
    if len(myList) > 1:
        # the point where the array is divided into two subarrays
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half. Sort the two halves
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        # Until we reach either end of either left or right, 
        # pick larger among elements Left and right and place them 
        # in the correct position at A[p..r]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # When we run out of elements in either Left or right,
        # pick up the remaining elements and put in A[p..mid]
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

n = int(input("Enter the no. of elements : "))
ipt = []
for i in range(n):
    ipt.append(int(input()))
mergeSort(ipt)
print(ipt)