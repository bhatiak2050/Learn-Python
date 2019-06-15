def merge(left, nl, right, nr, a):
        i,j,k = 0,0,0
        while i<nl and j<nr:
                if(left[i] <= right[j]):
                        a[k] = left[i]
                        k,i = k+1,i+1
                else:
                        a[k] = right[j]
                        k,j = k+1,j+1

        if(i<nl): a[k:] = left[i:]
        if(j<nr): a[k:] = right[j:]

def mergesort(list, n):
        if n<2: return

        mid = int(n/2)
        left = list[0:mid]
        right = list[mid:n]

        mergesort(left, mid)
        mergesort(right, n-mid)
        merge(left, mid, right, n-mid, list)

list = []
print("Enter the elements ('done' to break)")
while(True):
        inp = input()
        if inp == 'done': break
        elif not inp.isdigit(): continue
        else: list.append(int(inp))

mergesort(list, len(list))

print("\nThe sorted array is :")
print(list)
