print("Hello Python from Visual Studio Code!")
print("Hello world!")
# Вывести на экран пять строк из нулей, количество нулей в каждой строке равно номеру строки, 
# нули между собой разделять точкой с запятой. 
for i in range(6):
    print(*['0']*i, sep=';')