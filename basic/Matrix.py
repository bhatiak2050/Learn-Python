print("Enter the size of the matrix")
r = int(input())
c = int(input())

matrix = [0] * r

print("Enter the elements: ")
for i in range(0, r):
        matrix[i] = [0] * c
        for j in range(0, c):
                matrix[i][j] = int(input())

print(matrix)
for i in range(0,r):
        for j in range(0,c):
                print(matrix[i][j], end=" ")
        print()
