# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def simple_nums():
    for i in range(3, 100, 2):
        for j in range(3, i):
            if i % j == 0:
                break
        else:
            yield i
count = 0
a = simple_nums()
n = int(input("количество: "))
print(a)
while (count < n):
    print(next(a))
    count += 1