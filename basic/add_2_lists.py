n=5
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = []

for i in range(0, n):
        list3.append(0)  #This is required as list3 must be initialised with n elements before using
        list3[i] = list1[i] + list2[i]
print(list3)
