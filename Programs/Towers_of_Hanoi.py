def toh(n, beg, aux, end):
	if n==1:
		print("Disk 1: %s -> %s" % (beg, end))
		return
	toh(n-1, beg,end,aux)
	print("Disk %d: %s -> %s" % (n, beg, end))
	toh(n-1, aux,beg,end)

n = int(input("Enter the number of disks: "))
toh(n, 'A', 'B', 'C')
