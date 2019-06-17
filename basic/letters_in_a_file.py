fhand = open('words.txt')
letdict = dict()
for line in fhand:
        letters = list(line)
        for letter in letters:
                letdict[letter] = letdict.get(letter, 1) + 1 #value = dict.get(key, default)

print("Letter\tCount")
for key in letdict:
        print("%s\t%d" % (key, letdict[key]))
