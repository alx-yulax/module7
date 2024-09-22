print('Задача 7. Пропавшая карточка')

# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
#
# Вводится число N,
# далее еще N − 1 чисел:
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

# Пример:
# Введите количество карточек: 5
# Введите номер оставшейся карточки: 1
# Введите номер оставшейся карточки: 4
# Введите номер оставшейся карточки: 5
# Введите номер оставшейся карточки: 3

# Номер пропавшей карточки: 2

total_cards = int(input("Введите количество карточек: "))
missing_card = total_cards
remaining_sum = 0
for number_card in range(1, total_cards):
    card = int(input("Введите номер оставшейся карточки: "))
    missing_card += number_card - card
print(f"Номер пропавшей карточки: {missing_card}")