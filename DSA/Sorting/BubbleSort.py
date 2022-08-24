def BubbleSort(lst,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j+1],lst[j] = lst[j],lst[j+1]
            print(lst)
    return lst
n = int(input("Enter the no. of elements : "))
ipt = []
for i in range(n):
    ipt.append(int(input()))
print(BubbleSort(ipt,n))