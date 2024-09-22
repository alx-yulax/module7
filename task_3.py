print('Задача 3. Факториал')

# Мы всё ближе и ближе подбираемся к серьёзной математике.
# Одна из классических задач - задача на нахождение факториала числа.
# И в будущем мы с ней ещё встретимся.
#
# Дано натуральное число N. Напишите программу, которая находит N! (N факториал)
#
# Запись N! означает следующее:
#
# N! = 1 * 2 * 3 * 4 * 5 * … * N
#
# Пример:
#
# Введите число: 5
# Факториал числа 5 равен 120

number = int(input("Введите число: "))
factorial = 1
for current_number in range(1, number + 1):
    factorial *= current_number
print(f"Факториал числа {number} равен {factorial}")
