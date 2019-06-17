def knapsack(n, max_cap, price, weight):
	T = [0] * (n+1)

	for i in range(n+1): T[i] = [0] * (max_cap+1)

	for i in range(n+1):
		for j in range(max_cap+1):
			if i == 0 or j == 0:
				T[i][j] = 0
			elif weight[i-1] <= j:
				T[i][j] = max(T[i-1][j], price[i-1] + T[i-1][j-weight[i-1]])
			else:
				T[i][j] = T[i-1][j]

	'''
	for i in range(n+1):
		for j in range(max_cap+1):
			print(T[i][j], end=" ")
		print()
	'''
	print("The Maximum Profit is %d" % T[n][max_cap])

#Main Block
n = int(input("Enter the number of items: " ))
max_cap = int(input("Enter the Max cap: "))

price, weight = [], []

print("Enter the prices: ")
for i in range(n):
	price.append(int(input()))

print("Enter the weights: ")
for i in range(n):
	weight.append(int(input()))

knapsack(n, max_cap, price, weight)
