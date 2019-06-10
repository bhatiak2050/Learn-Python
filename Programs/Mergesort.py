def merge(left, nl, right, nr, a):
	i=0;j=0;k=0
	while i<nl and j<nr:
		if(left[i] <= right[j]):
			a[k] = left[i]
			k+=1; i+=1
		else:
			a[k] = right[j]
			j+=1; k+=1
	while i<nl:
		a[k] = left[i]
		i+=1; k+=1
	while j<nr:
		a[k] = right[j]
		j+=1; k+=1

def mergesort(list, n):
	if n<2: return

	mid = int(n/2)
	left = []
	right = []

	for i in range(0,mid):
		left.append(0)
		left[i] = list[i]
	for i in range(mid, n):
		right.append(0)
		right[i-mid] = list[i]

	mergesort(left, mid)
	mergesort(right, n-mid)
	merge(left, mid, right, n-mid, list)

list = []
print("Enter the number of elements: ")
n = int(input())
print("Enter the elements: ")
for i in range(0,n):
	list.append(0)
	list[i] = int(input())

mergesort(list, n)

print("\nThe sorted array is :")
for i in range(0,n):
	print(list[i], end=" ")
