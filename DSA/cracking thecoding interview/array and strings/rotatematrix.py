n= int(input())
arr=[]
for i in range(n):
    b=[]
    for j in range(n):
        b.append(int(input()))
    arr.append(b)
print(arr)

# transpose
for i in range(n):
    for j in range(i,n):
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
print(arr)

# rotate 90
for i in range(n//2):
    for j in range(n):
        arr[j][i],arr[j][n-i-1]=arr[j][n-i-1],arr[j][i]
print(arr)