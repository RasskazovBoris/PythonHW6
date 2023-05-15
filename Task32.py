a = int(input("Введите длину списка: "))
array = []
for i in range(a):
    b = int(input ("Введите значение: "))
    array.append(b)
print (array)
c = int(input("Введите начальное значение диапазона: "))
d = int(input("Введите конечное значение диапазона: "))
array2 = []
for i in range(len(array)):
    if array[i] >= c and array[i] <= d:
        array2.append(i)
print (array2)