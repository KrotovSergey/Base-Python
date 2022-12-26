num_zadacha = int(input('какую задачу проверить? (их всего 3)  '))
match num_zadacha:
    case 1:
        print('Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr".')
        print('То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.')


        input_str = input("ввдите строку: ")

        res = (lambda x: 'plr' in x)(input_str)

        print (res)

    case 2:
        print('Найти общий делитель')

        a = int(input('Введите а: '))
        b = int(input('Введите в: '))
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a

        print(a)
    case 3:
        print('Напишите программу, удаляющую из текста все слова, содержащие ""абв"".')

        str = 'ываыв ываывгр авьабв  абв авбываоро лфлл'
        print(str)

        result = str.split()

        result = filter(lambda x:'абв' not in x, result)

        print(*result)

        #print(str.translate({ord(i): None for i in 'абв'}))