while True: #даны три целых числа: a,b,c. Только два из них равны
  try: #обработка исключений
    a,b,c = int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))

    if (a==b and a!=c and b!=c)or(a==c and a!=b and b!=c)or(b==c and a!=b and a!=c): #условие: равны только два числа
      print('Справедливо!')
      break #выход из цикла, если все значения ввели правильно и условие соблюдено
    else:
      print('Не верно!')

  except ValueError:
    print('Введите целые числа!')
    continue #переход в начало цикла для повторного ввода значений, если не правильный формат значений или не соблюдено условие