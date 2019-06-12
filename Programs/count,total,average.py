total=0
count=0
average=0
number = input("Enter the numbers: ")
while(number != 'done'):
	try: number = int(number)
	except:
		print("Please enter a number")
		number=input()
		continue
	count +=1
	total = total + number
	average = total/count
	number = input()

print("Total",total)
print("Count",count)
print("Average",average)
