# Пространство имен.
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function() # всё работает
inner_function() # ошибка так как имя в локальной видимости