from main import find_nearest_element
my_array = [1, 5, 9, 15, 20]
target_value = int(input('Введите число: '))
nearest_element = find_nearest_element(my_array, target_value)
print(f"Ближайший элемент к {target_value}: {nearest_element}")