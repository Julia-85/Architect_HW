# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

st = 'drfhfgjgh'

dict_0 = {item: ord(item) for item in st}   # Тратит память
print(dict_0)

