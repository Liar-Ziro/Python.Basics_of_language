'''Задача-1: используя цикл запрашивайте у пользователя число пока оно не
станет больше 0, но меньше 10. После того, как пользователь введёт корректное
число, возведите его в степень 2 и выведите на экран. Например, пользователь
вводит число 123, вы сообщаете ему, что число не верное, и сообщаете об
диапазоне допустимых. И просите ввести заново. Допустим пользователь ввёл 2,
оно подходит, возводим в степень 2, и выводим.'''


while True:
    user = int(input('Введите число от 0 до 10: '))
    if 0 < user_number < 10:
        print('Результат:', user ** 2)
        break
    else:
        print('Число не верное. Диапазон допустимых значений от 0 до 10.')

