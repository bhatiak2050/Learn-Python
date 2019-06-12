string = "Hello World"
new_string = ''
for i in string:
        if i == 'e':
                new_string += 'o'
        elif i == 'o':
                new_string += 'e'
        else:
                new_string += i

string = new_string
print(string)
