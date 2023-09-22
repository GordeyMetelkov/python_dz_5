# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

path = "C:\Program Files (x86)\Internet Explorer\iexplore.exe"
def file_path(path: str):
    c = "d\d"
    c = c[1]
    *path_to_file, file = path.split(c)
    name = file.split('.')[0]
    extension = (file.split('.')[1])
    extension = f'.{extension}'
    return (c.join(path_to_file), name, extension)
print(file_path(path))