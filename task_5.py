print('Задача 5. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

# (среднее арифметическое можно посчитать поделив сумму подходящих чисел на их количество)

number_a = int(input("Введите число a: "))
number_b = int(input("Введите число b: "))

sum_numbers = 0
count_numbers = 0

for current_number in range(number_a, number_b + 1):
    if current_number % 3 == 0:
        sum_numbers += current_number
        count_numbers += 1

if count_numbers > 0:
    average = sum_numbers / count_numbers
    print(f"Среднее арифметическое чисел, кратных 3, на отрезке [{number_a}; {number_b}] равно {average:.2f}")
else:
    print("На отрезке нет чисел, кратных 3.")
