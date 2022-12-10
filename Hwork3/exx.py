num_zadacha = int(input('какую задачу проверить? (их всего 5)  '))
match num_zadacha:
    case 1:
        print(f'Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,\nстоящих на нечётной позиции.')

        lst1 = [2, 3, 4, 5, 6]
        summ1 = 0
        lst11 = []
        for i in lst1:
            if i%2!=0:
                summ1 += i
                lst11.append(i)    
        print(f' в списке {lst1} на нечетных позициях элементы = {lst11} а их суммаа = {summ1}')

    case 2: 
        print(f"Напишите программу, которая найдёт произведение пар чисел списка.\nПарой считаем первый и последний элемент, второй и предпоследний и т.д.")
                 
        lst2 = [int(i) for i in input("Введите числа через пробел: ").split()]
        new_lst2 = []
        size = len(lst2)
        for i in range(size // 2 if size % 2 == 0 else size // 2 + 1): 
            new_lst2.append(lst2[i] * lst2[size - i - 1])  
        print(lst2, '=>', new_lst2)
        
    case 3: 
        print(f"Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением \nдробной части элементов.")

        lst3 = [1.1, 1.2, 3.1, 5, 10.01,]
        lst31 = [lst3[i] - int(lst3[i]) for i in range(len(lst3))]
        print(f'разнница между мин и маакс знначением в списке {lst3} = {max(lst31) - min(lst31)}')

    case 4: 
        print("Напишите программу, которая будет преобразовывать десятичное число в двоичное.")


        dvoich = ""
        desat = int(input("Введите число для преобразовывания десятичного числа в двоичное:  "))
        while desat != 0:
            dvoich = str(desat%2) + dvoich
            desat //=2
        print(dvoich)

    case 5: 
        print("Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")


        
        n=int(input("Введите число для создания списка чисел Фибоначчи:  "))           
        
        def get_fibonacci(n):
            fibo_nums = []
            a, b = 1, 1
            for i in range(n-1):
                fibo_nums.append(a)
                a, b = b, a + b
                a, b = 0, 1
            for i in range (n):
                fibo_nums.insert(0, a)
                a, b = b, a - b
            return fibo_nums

        fibo_nums = get_fibonacci(n)
        print(get_fibonacci(n))
        print(fibo_nums.index(0))


