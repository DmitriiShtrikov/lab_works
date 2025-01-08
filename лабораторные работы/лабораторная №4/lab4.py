import math
number = int(input('введите число '))
sqrt_value = math.sqrt(number)
print(f"Квадратный корень из {number} равен {sqrt_value}.")

import datetime
now = datetime.datetime.now()
print(f"Текущая дата и время: {now}")

import my_module

result = my_module.add_numbers(int(input('ведите число 1: ')),int(input('ведите число 2: ')) )
print(f"Сумма: {result}")