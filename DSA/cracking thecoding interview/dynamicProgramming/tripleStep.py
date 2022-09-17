def countWays(n):
	way = [0] * (n + 1)
	way[0] = 1
	way[1] = 1
	way[2] = 2

	for i in range(3, n + 1):
		way[i] = way[i - 1] + way[i - 2] + way[i - 3]

	return way[n]

n = int(input("Enter the number of staircase: "))
print(countWays(n))