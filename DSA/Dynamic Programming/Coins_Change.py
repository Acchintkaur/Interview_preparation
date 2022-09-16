def ways(coins,n,k):
    ways = [0 for i in range(k+1)]
    ways[0]=0
    for j in range(1,k+1):
        minimum = k
        for i in range(n):
            if coins[i]<=j:
                minimum = min(minimum,1+ways[j-coins[i]])
            ways[j] = minimum
    return ways[k]


k= int(input("Enter the sum required: "))
n= int(input("\nEnter the denominations of coins: "))
coins = []
for i in range(n):
    coins.append(int(input()))
print(ways(coins,n,k))