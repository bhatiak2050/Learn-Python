filename = input("Enter the filename: ")
fhand = open(filename)
words = []
for line in fhand:
	list = line.split()
	for word in list:
		if word not in words:
			words.append(word)


words.sort()
print(words)
