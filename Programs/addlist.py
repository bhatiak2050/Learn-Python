def addlist(list):
        sum=0
        for i in list:
                sum += i
        return sum

print("Enter the numbers to sum (in newlines): ")
print("Press Enter twice to break")
list = []
while(True):
        try: list.append(int(input()))
        except: break

print("The sum is", addlist(list))
