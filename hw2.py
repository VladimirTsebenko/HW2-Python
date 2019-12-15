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


# 3. Дан текстовый файл. Создать новый файл, каждая строка которого получается
#  из соответствующей строки
#  исходного файла перестановкой слов в обратном порядке.

src = open("words.txt", "r")
text = src.readlines()
print (text)
for lines in range(0, len(text)):
    text[lines] = text[lines].split()[::-1]
dist = open("rewords.txt", "w")
for line in text:
    line = " ".join(line)+ "\n"
    dist.write(line)
src.close()
dist.close()



# 4. Написать функцию word_counter которая считает количество слов в тексте.
#  Функция должна принимать либо путь к файлу, либо строку с текстом

str = 'a e r t y y se sfd sdfsf'    

def word_counter(s):
    words = str.split()
    print('Number of words: ',len(words))

word_counter(str)

