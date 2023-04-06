'''Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
первое число, второе число и операцию, после чего применяет операцию к введённым числам
("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
'''
a = float(input())
b = float(input())
c = str(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
elif c == '*':
    print(a * b)
elif c == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif c == 'pow':
    print(a ** b)
elif c == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
else:
    print('Ошибка')

