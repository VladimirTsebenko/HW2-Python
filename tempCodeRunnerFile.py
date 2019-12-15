import os
def word_counter(filename):
     
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", " ").replace(".", " ").replace("?", " ").replace("!", " ").replace(";", " ")
    words = text.split()
    words.sort()
    return words
 
def main():
    choice = int(input("Введите 1 что бы прочитать файл или 2 что бы ввести строку: "))

    if  choice <= 1:
        filename = input("Введите путь к файлу: ")
        if not os.path.exists(filename):
            print("Указанный файл не существует")
        else:
            words = word_counter(filename)
            print("Кол-во слов: %d" % len(words))
    else:
        listWords = input("Введите слова: ")
        listWords = listWords.replace(",", " ").replace(".", " ").replace("?", " ").replace("!", " ").replace(";", " ")
        w_list = listWords.split()
        print("Кол-во слов: %d" % len(w_list))


if __name__ == "__main__":
    main()