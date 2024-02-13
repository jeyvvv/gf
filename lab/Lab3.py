string = input("Введите строку: ")
pattern = input("Введите образец: ")
positions = []
for i in range(len(string) - len(pattern) + 1):
  if string[i:i +  len(pattern)]==pattern:
    positions.append(i)
print('Positions:', positions)
