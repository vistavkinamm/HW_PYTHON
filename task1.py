# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

x = input('Введите число ')

def summa(x):                            
    if float(x) < 0:                            
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел заданного числа: {summa(x)}')