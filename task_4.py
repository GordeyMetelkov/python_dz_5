# Создайте функцию генератор чисел Фибоначчи

def fab():
    first = 0
    sec = 1
    for i in range(100):
        yield sec
        first, sec = sec, sec + first
tmp = fab()
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))