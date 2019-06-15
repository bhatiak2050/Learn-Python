list = [1,2,3]
list.extend([4,5])
print(list)

list = [1,2,3]
list.append([4,5])
print(list)

list = [8,5,6,9,7,2,4,1,3]
list.sort()
print(list)

list.reverse()
print(list)

print(list[4:7])
list[4:7] = [0,0,0]
print(list)

list = [1,2,3,4,5]
del list[1:3]
print(list)

list = [1,3,5,'7','9']
list.pop(2)
list.remove('9')
print(list)
