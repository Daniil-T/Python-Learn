'''Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.'''
digits = 1
while digits != 0:
    digits = int(input())
    if digits < 10:
        continue
    if digits > 100:
        break
    print(digits)

'''
Интересный вариант решения, где все результаты выводятся в некст строчке
b = ''

while True:
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        b = b + str(a) + '\n' #Получается при первой итерации цикла мы к пустой строке прибавляем число введенное и переведенное в строку, вторая итерация это уже прибавление к результату первой итерации и тд
print (b)
'''