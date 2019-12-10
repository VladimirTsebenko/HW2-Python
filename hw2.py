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

f = open("numbers.txt", "r")
numbers = f.read()
print(numbers)
print (type(numbers))
f.close()

array = [int(sub.split()[1]) for sub in numbers]

# for line in numbers:  # read rest of lines
#   array.append([int(x) for x in line.split()])
print(array)
print(type(array))
for i in array:
    if (i % 2 != 0):
        array.remove(i)
print (array)


# 3. Дан текстовый файл. Создать новый файл, каждая строка которого получается из соответствующей строки
#  исходного файла перестановкой слов в обратном порядке.

f = open("words.txt", "r")
text = f.read()
print(text)
f.close()

# 4. Написать функцию word_counter которая считает количество слов в тексте.
#  Функция должна принимать либо путь к файлу, либо строку с текстом



