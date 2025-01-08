from my_package import math_operations, string_operations

sum_result = math_operations.add(int(input('ведите первое число для нахождения сумм: ')), int(input('ведите второе число для нахождения сумм: ')))
diff_result = math_operations.subtract(int(input('ведите первое число для нахождения разности: ')), int(input('ведите второе число для нахождения разности: ')))
print(f"Сумма: {sum_result}, Разность: {diff_result}")

capitalized = string_operations.capitalize_string(input('введите строку:'))
reversed_str = string_operations.reverse_string(input('ведите стоку (она будет реверсирована)'))
print(f"Заглавная строка: {capitalized}, Обратная строка: {reversed_str}")