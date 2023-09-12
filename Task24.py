"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

Пример:
4 -> 1 2 3 4

9
"""

n=(int(input("Введите число кустов на грядке: ")))
list1=[]
for i in range(n):
    num = int(input(f"Введите число ягод на {i+1}-м кусте: "))
    list1.append(num)

# print(list1)

max = 0

for _ in range(n):
    sum3 = sum(list1[0:3])
    if sum3 > max:
        max = sum3
#    print(list1[0:3])
    list1.insert(0, list1.pop())

print(max)