print('Задача 6. Замечательные числа')

# Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.

# Пояснение:
# 15 -> 1*5*3 = 15 - получившееся число равно оригиналу, значит число надо вывести
# 16 -> 1*6*3 = 18 - число выводить не нужно, 18 не равно 16

for number in range(10, 100):
    first_digit = number // 10
    second_digit = number % 10
    result = first_digit * second_digit * 3
    if number == result:
        print(number)