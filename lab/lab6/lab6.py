with open("input.txt","r") as input_file, open("output.txt","a") as output_file:
    for line in input_file:
     words = line.split()
     five_letter_words = [int(input("Введите длину слова: "))]
     output_file.write(" ".join(five_letter_words) + '\n')
print("Копирование успешно")
