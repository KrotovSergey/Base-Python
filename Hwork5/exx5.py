num_zadacha = int(input('какую задачу проверить? (их всего 5)  '))
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