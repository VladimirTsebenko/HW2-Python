f = open('numbers.txt', 'r+')
lines = f.read().split()
numbers =[int(e.strip()) for e in lines]
#print(numbers)
odd = []
for num in numbers:
    if(num % 2 != 0):
        odd.append(num)
        f.seek(0)
        f.write(str(odd))
        f.truncate()
        f.flush()
f.close()
#print(odd)