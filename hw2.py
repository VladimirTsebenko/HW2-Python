# 1.Рассчитать последовательность фибоначчи, длину ряда задает пользователь

number = int(input("Enter Fibonacci length: "))
print ("Fibonacci number of: ", number, "is: ",
       round(((5**(0.5)+1)/2)**number/(5**(0.5))))

p = range(number+1)
fibonacci = []
for i in p:
    if(i == 0):
        n = 0
        fibonacci.append(n)
    elif(i == 1):
        n = 1
        fibonacci.append(n)
    elif(i > 1):
        n = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(n)
print("Fibonacci sequence is: ", fibonacci)

# 2. Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

numbers = [line.rstrip('\n') for line in open('numbers.txt')]
print(numbers)
print(type(numbers))
for i  in numbers:
    	if(i%2 == 0):
	        numbers.remove(i)
print(numbers)
print(type(numbers))

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



# 3. Дан текстовый файл. Создать новый файл, каждая строка которого получается из соответствующей строки
#  исходного файла перестановкой слов в обратном порядке.

f = open("words.txt", "r")
text = f.read()
print(text)
f.close()

# 4. Написать функцию word_counter которая считает количество слов в тексте.
#  Функция должна принимать либо путь к файлу, либо строку с текстом

list = [11, 22, 33, 44, 55]

# print original list
print ("Original list:")
print (list)
print (type(list))

# loop to traverse each element in the list
# and, remove elements
# which are EVEN (divisible by 2)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)

# print list after removing EVEN elements
print ("list after removing EVEN numbers:")
print (list)
print (type(list))