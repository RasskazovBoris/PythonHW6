a = int(input("Введите первый элемент: "))
b = int(input("Введите разность: "))
c = int(input("Введите количество элемнтов: "))
array = []
for i in range(c):
    array.append (a + (i)*b)
for i in array:
    print (i)
