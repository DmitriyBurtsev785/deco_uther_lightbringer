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
