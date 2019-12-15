f = open('numbers.txt', 'r+')
lines = f.read().split()
numbers =[int(e.strip()) for e in lines]

print(lines)
print(type(lines))
print(type(lines[1]))
print(numbers)
print(type(numbers))
for i  in numbers:
    if(i%2 == 0):
	     numbers.remove(i)
print(numbers)
print(type(numbers))
print(type(numbers[1]))
f.seek(0)

f.write(str(numbers))
f.truncate()
f.close