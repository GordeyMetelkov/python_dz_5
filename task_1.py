# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def simple_nums():
    lst = set()
    lst.add(2)
    for i in range(3, 100, 2):
        for j in range (2, i):
            if i % j != 0:
                lst.add(i)
    for i in lst:
        yield i
count = 0
a = simple_nums()
n = int(input("количество: "))
while (count < n):
    print(next(a))
    count += 1