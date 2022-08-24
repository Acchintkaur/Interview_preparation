m= int(input())
n= int(input())
a=[]
for i in range(m):
    b=[]
    for j in range(n):
        b.append(int(input()))
    a.append(b)
print(a)
zero_rows = []
zero_cols = []
for i in range(m):
    for j in range(n):
        if a[i][j] == 0:
            zero_cols.append(j)
            zero_rows.append(i)
for i  in range(m):
    for j in range(n):
        if i in zero_rows:
            a[i][j]=0
        if j in zero_cols:
            a[i][j]=0
print(a)