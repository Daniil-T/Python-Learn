'''
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет,
счастливый ли ему попался. Билет считается счастливым, если сумма первых трех цифр совпадает
с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит
равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
'''
TicketNumber = input()
secondDigitIsOne = int(TicketNumber[0]) + int(TicketNumber[1]) + int(TicketNumber[2])
secondDigitIsTwo = int(TicketNumber[3]) + int(TicketNumber[4]) + int(TicketNumber[5])
if secondDigitIsOne == secondDigitIsTwo:
    result = 'Счастливый'
else:
    result = 'Обычный'
print(result)
#############