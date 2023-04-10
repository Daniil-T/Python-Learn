'''Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в
строке, и после первого введенного нуля выводит сумму полученных на вход чисел.'''

''' 
Первый вариант, рабочий
digits = int(input())
if digits == 0:
    print(digits)
else:
    digits_2 = 1
    while digits_2 != 0:
        digits_2 =int(input())
        digits += digits_2
    print(digits)
'''
'''Второй вариант, лучше и рабочий'''
digits = int(input())
sum = 0
while digits != 0:
    sum += digits
    digits = int(input())
print(sum)