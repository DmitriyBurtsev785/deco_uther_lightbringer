# Блок 1
# Easy

# Задача 1
# Написать простую функцию, которая на вход принимает строку ('test') и целое число (3),
# а возвращает строку вида 'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.

def multiply_string_by_number(line: str, number: int) -> str:
    current_line = ''
    for i in range(number):
        if i % 2 == 1:
            current_line += line.upper()
        else:
            current_line += line
    return current_line

print(multiply_string_by_number('test', 3))


# Задача 2
# Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?

variable = multiply_string_by_number
print(variable) # ссылка на ячейку в памяти, где хранится функция multiply_string_by_number



# Задача 3
# Вызвать функцию суммирования через переменную, в которую вы только что её записали.

print(variable('test', 3))



# Medium

# Задача 1
# Написать функцию, которая на вход будет принимать произвольное количество аргументов и возвращать их сумму.

def calculation_of_sum_of_arguments(*args, **kwargs):
    return sum(args)

print(calculation_of_sum_of_arguments(1, 2, 3, 4))

# Задача 2
# В сигнатуре функции объявить 4 обязательных аргумента, но оставить возможность передавать в неё сколько угодно
# дополнительных аргументов.

def calculation_of_sum_of_arguments_2(a, b, c, d, *args, **kwargs):
    return sum([a, b, c, d, *args]) + sum([value for key, value in kwargs.items()])

# Попробуйте вызвать функцию в следующих ситуациях и объясните результат:
#    - прокинуть в функцию только 1 аргумент


# print(calculation_of_sum_of_arguments_2(1))
# Ошибка. Мы прописали 4 обязательных аргументов, а передаём только 1.



#    - прокинуть аргументы таким образом, чтобы обязательный аргумент был передан одновременно позиционно и по ключу

print(calculation_of_sum_of_arguments_2(a=1, b=2, c=3, d=4))

#    - создать кортеж со значениями и распаковать его при вызове функции с помощью *

my_tuple = (1, 2, 3, 4)
print(calculation_of_sum_of_arguments_2(*my_tuple))


# создать словарь со значениями и распаковать его при вызове функции с помощью * и **: что наблюдаете? Почему?

# не понял, что нужно делать.....



