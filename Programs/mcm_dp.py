INT_MAX = 999

def mcm(p, n):
        m = [0] * n
        for i in range(n): m[i] = [0] * n

        for L in range(2,n):
                for i in range(1, n-L+1):
                        j = i+L-1
                        m[i][j] = INT_MAX
                        for k in range(i,j):
                                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
                                if q < m[i][j]: m[i][j] = q

        print("Minimum number of multiplications is %d " % m[1][n-1])

n = int(input("Enter the number of matrices: ")) + 1
p = []
print("Enter the size arrray: ")
for i in range(n): p.append(int(input()))

mcm(p, n)
