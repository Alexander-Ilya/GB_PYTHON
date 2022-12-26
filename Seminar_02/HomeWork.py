# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2
import random

random.seed

numberOfCoins = int(input('Задайте количество монет: '))
positionOfCoins = [random.randint(0, 1) for i in range(numberOfCoins)]
print(positionOfCoins)
positionOfCoinsZero = 0
for i in range(numberOfCoins):
    if positionOfCoins[i] == 0:
        positionOfCoinsZero += 1
if positionOfCoinsZero < numberOfCoins - positionOfCoinsZero:
    print(positionOfCoinsZero)
else:
    print(numberOfCoins - positionOfCoinsZero)

# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
S, P = int(input('Сумма: ')), int(input('Произведение: '))
num1 = 0
num2 = 0
while num1 <= S // 2 + 1:
    while num2 <= P:
        if (num1 + num2 == S) and (num1 * num2 == P):
            print(f'Числа {num1} и {num2}')
            break
        else:
            num2 += 1
        num1 += 1
    break
else:
    print('Таких чисел нет')

# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
# 5
# 1 2 4
# 17
# 1 2 4 8 16
number = int(input('Задайте число: '))
degreeOfNumber = 0

while True:
    if 2 ** degreeOfNumber < number:
        print(2 ** degreeOfNumber)
        degreeOfNumber += 1
    else:
        break
