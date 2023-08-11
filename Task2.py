#Напишите функцию принимающую на вход только ключевые параметры(kwargs) и возвращающую словарь,
 # где ключ — значение переданного аргумента, а значение — имя аргумента.
 # Если ключ не хешируем, используйте его строковое представление.
 # reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}


def kwargs_dictionary(**reverse_kwargs):
     result = {}
     for key, value in reverse_kwargs.items():
         try:
             result[value] = key
         except:
             result[str(value)] = key
     return result


print(kwargs_dictionary(rev=True, acc="YES", stroka=4))  