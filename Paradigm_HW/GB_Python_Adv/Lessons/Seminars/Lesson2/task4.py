# ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

import math
import decimal    # 28 знаков для числа по умолчанию
import fractions   # обыкновенные дроби

decimal.getcontext().prec = 48
print(decimal.Decimal(math.pi))
print('3.141592653589793238462643383279502884197169399375')
