list = []
number = input("Enter the numbers ('done' to stop):\n")
while(number != 'done'):
        try: list.append(int(number))
        except: print("Please enter a number")
        number = input()

largest = None
smallest = None
for i in list:
        if largest is None or i > largest:
                largest = i
        if smallest is None or i < smallest:
                smallest = i

print("Largest =",largest)
print("Smallest =", smallest)
