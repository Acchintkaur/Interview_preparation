def LCS(X, Y, m, n, lookup):
    if m == 0 or n == 0:
        return str()
    if X[m - 1] == Y[n - 1]:
        return LCS(X, Y, m - 1, n - 1, lookup) + X[m - 1]
 
    if lookup[m - 1][n] > lookup[m][n - 1]:
        return LCS(X, Y, m - 1, n, lookup)
    else:
        return LCS(X, Y, m, n - 1, lookup)

def LCSLength(X, Y, m, n, lookup):
    for i in range(1, m + 1):  
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
 
if __name__ == '__main__':
 
    X = input()
    Y = input()
 
    m = len(X)
    n = len(Y)
    lookup = [[0 for x in range(n + 1)] for y in range(m + 1)]
    LCSLength(X, Y, m, n, lookup)
    print(LCS(X, Y, m, n, lookup))