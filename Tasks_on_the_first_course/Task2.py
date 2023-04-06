'''
Напишите программу, принимающую на вход целое число, которая выводит True,
если переданное значение попадает в интервал
(−15,12]∪(14,17)∪[19,+∞)
и False в противном случае (регистр символов имеет значение).

Обратите внимание на разные скобки, используемые для обозначения интервалов.
В задании используются полуоткрытые и открытые интервалы. Подробнее про это вы
можете прочитать, например, на википедии (полуинтервал, промежуток).
∪ - знак объединения множеств, т.е. число должно лежать во промежутчке всех множеств представленных в скобках.
'''

a = float(input())
if a >= 19.0:
    print('True')
elif 14.0 < a < 17.0:
    print('True')
elif (-15.0) < a <= 12.0:
    print('True')
else:
    print('False')