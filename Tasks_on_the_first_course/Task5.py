'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на
консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
'''
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))
print(min(a, b, c))
if a <= b:
    if b >= c:
        if c <= a:
            print(a)
        else:
            print(c)
    else:
        print(b)
else:
    if a >= c:
        if b >= c:
            print(b)
        else:
            print(c)
    else:
        print(a)