# Для наглядности расстановки приоритетов операций - арифметические операции выше по приоритету, чем операции сравнения
x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)
print((y > (x * x)) or (y >= (2 * x) and x < y))

#Некст задача
a = True
b = False
result_1=(a and b or not a and not b)
result_2=((a and b) or (not a and not b))

print(result_1)
print(result_2)
# Скобки в первой и второй задачке расставил для проверки правильности понимания того, как программа распределяет приоритет действий
