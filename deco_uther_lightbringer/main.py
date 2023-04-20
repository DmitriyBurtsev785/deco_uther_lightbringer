# Блок 1
# Easy
# Задача 1

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





