num_zadacha = int(input('какую задачу проверить? (их всего 3)  '))
match num_zadacha:
    case 1:
        print('Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.')
        
        number = input().split()
        nu = list(filter(lambda x: (-99 <= int(x) <= -10) or (10 <= int(x) <= 99), number))
        print(*nu) 

    case 2:
        print('Дан список, вывести отдельно буквы и цифры')
        print('a = (a,b,2,3,c)')

        a = ( "a", 'b', '2', '3' ,'c')

        b= filter(str.isalpha, a)
        c= filter(str.isdigit, a)

        print(*b)
        print(*c)

    case 3:

        print("Преобразовать наборы списков \nusers = ['user1','user2','user3','user4','user5'] \nids = [4, 5, 9, 14, 7] \nsalary = [111,222,333]")
        print("В другой набор и вернуть в мсходное положение")

        users = ['user1','user2','user3','user4','user5']
        ids = [4, 5, 9, 14, 7]
        salary = [111,222,333]

        a,b,c = map(list,zip(users, ids, salary))
        print(a,b,c, sep="\n")
        a,b,c= map(list,zip(a,b,c))

        print(a,b,c, sep="\n")