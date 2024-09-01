# 1st program
# Задача 1: Арифметика
result1 = (9 ** 0.5) * 5
print(result1)  # Ожидаемый результат: 15.0

# 2nd program
# Задача 2: Логика
result2 = 9.99 > 9.98 and 1000 != 1000.1
print(result2)  # Ожидаемый результат: True

# 3rd program
# Задача 3: Школьная загадка
without_priority = 2 * 2 + 2
with_priority = 2 * (2 + 2)
comparison_result = without_priority == with_priority
print(without_priority)   # Ожидаемый результат: 6
print(with_priority)      # Ожидаемый результат: 8
print(comparison_result)  # Ожидаемый результат: False

# 4th program
# Задача 4: Первый после точки
number = '123.456'
# Преобразование строки в число с плавающей точкой
float_number = float(number)
# Умножаем на 10, чтобы цифра после точки стала целой частью
shifted_number = float_number * 10
# Преобразуем в целое число и получаем остаток от деления на 10
first_digit_after_decimal = int(shifted_number) % 10
print(first_digit_after_decimal)  # Ожидаемый результат: 4



