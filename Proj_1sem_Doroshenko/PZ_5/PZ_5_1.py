#Составить функцию,которая выведет на экран строку,задаваемое с клавиатуры число символов.

def amount():
    try:
        a = int(input('Введите целое число: '))
        c = '*'
        print(a * c)  # Выводит число символов, заданное вами
    except:
        print('Введите целое число!')


amount()