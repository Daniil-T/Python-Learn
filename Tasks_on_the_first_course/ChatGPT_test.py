# функция для сложения двух чисел
def add(x, y):
   return x + y

# функция для вычитания двух чисел
def subtract(x, y):
   return x - y

# функция для умножения двух чисел
def multiply(x, y):
   return x * y

# функция для деления двух чисел
def divide(x, y):
   return x / y

# ввод пользователя
print("Выберите операцию.")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

# получение входных данных от пользователя
choice = input("Введите номер операции (1/2/3/4): ")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# операции калькулятора
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Неправильный ввод, попробуйте снова.")