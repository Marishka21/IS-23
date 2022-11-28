# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого положительного числа К на обратной
# (К-параметр целого типа, являющийся одновременно входным и выходным). С помощью этой функции поменять порядок
# следования цифр на обратной для каждого из пяти данных чисел.

import math

def InvertDigits(k):
 a = 0
 while k != 0:
  a = a * 10 + math.fmod(k, 10)
  k = int(k/10)
 return a

i = 0
while i < 5:
 print('Введите число К: ')
 k = int(input())
 i = i + 1
 print('Обратный порядок цифр: ', int(InvertDigits(k)))
 break
