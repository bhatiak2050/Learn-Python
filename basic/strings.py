name = "Sam"
age = 24
job = "Designer"
print("Name\t: %s\nAge\t: %s\nJob\t: %s" % (name, age, job))

name = "Hello World"
print(len(name))                #Length of the string
print(name.index('W'))          #Index of character 'W'
print(name.count('o'))          #No of occurances of 'o'
print(name[3:7])                #Substring from index 3 to 6
print(name[:5])                 #Substring from start to index 5
print(name[5:])                 #Substring from index 5 to end
print(name[-3:])                #Substring from 3rd from last to end
print(name[:-3])                #Substring from start to 3rd from last
print(name[0:len(name):2])      #Substring from 0 to end skipping one character
print(name[0::2])               #Same as above, format: [start:stop:step]
print(name[::-1])               #Reverse a string, step is -1
print(name.upper())             #Converts string to uppercase
print(name.lower())             #Converts string to lowercase
print(name.startswith("Hello")) #Returns true if string starts with Hello, else false\
print(name.endswith("Hello"))   #Returns true if string ends with Hello, else false
print(name.split(" "))          #Splits the string into a list using " " as the delimeter
