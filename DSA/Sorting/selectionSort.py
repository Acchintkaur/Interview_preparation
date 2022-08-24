def selectionSort(a,n):
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j] = a[j], a[i]
    return a
n = int(input("Enter the no. of elements : "))
ipt = []
for i in range(n):
    ipt.append(int(input()))
print(selectionSort(ipt,n))