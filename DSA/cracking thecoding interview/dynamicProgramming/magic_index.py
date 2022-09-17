def magicIndex(arr,low,high):
    if high>=low:
        mid = (low+high)//2
        if mid == arr[mid] :
            return mid
        # if index<midvalue move to right part of array
        elif mid < arr[mid]:
            return magicIndex(arr,low,mid-1)
        # if index>midvalue move to left part of array
        else:
            return magicIndex(arr,mid+1,high)

    return -1


n= int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
print(magicIndex(arr,0,n-1))