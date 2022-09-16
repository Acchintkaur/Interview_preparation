def LCS(X,Y):
    m,n = len(X),len(Y)
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if X[i-1]==Y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    lcs=""
    i=m
    j=n
    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            lcs+=X[i-1]
            i-=1
            j-=1
        elif X[i-1]>Y[j-1]:
            i-=1
        else:
            j-=1
    return lcs[::-1]
X=input()
Y=input()
print(LCS(X,Y))