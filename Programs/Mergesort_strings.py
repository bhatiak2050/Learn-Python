def merge(left, nl, right, nr, a):
	i=0;j=0;k=0

	while i<nl and j<nr:
		if(left[i] <= right[j]):
			a[k] = left[i]
			i+=1; k+=1
		else:
			a[k] = right[j]
			j+=1; k+=1
	while i<nl:
		a[k] = left[i]
		i+=1; k+=1
	while j<nr:
		a[k] = right[j]
		j+=1; k+=1

def mergesort(names):
	n = len(names)
	if n<2: return

	mid = int(n/2)
	left = []
	right = []

	for i in range(0, mid):
		left.append(names[i])

	for i in range(mid, n):
		right.append(names[i])

	mergesort(left)
	mergesort(right)
	merge(left, mid, right, n-mid, names)

names = []
name = input("Enter the names ('done' to stop)\n")
while(name != 'done'):
	names.append(name)
	name = input()

mergesort(names)

print("\nThe names in alplabetical order are:")
for name in names:
	print(name)
