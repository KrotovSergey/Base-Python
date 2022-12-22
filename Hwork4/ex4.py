from random import randint

num_zadacha = int(input('какую задачу проверить? (их всего 5)  '))
match num_zadacha:
    case 1:
        print(f'Вычислить число c заданной точностью d')

        k = int(input('введдите до скольки заков после запятой вычислять: '))
        print(f'Вычислим на примере формулы L = 2πr при r = 3')
        p = float(3.1415926535)
        L = 2*p*3
        print(round(L,k))     

        # a = int(input('введите нужную точность 1#= '))
        # pi_target = 0
        # for i in range(1, 1000000):
        #     pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
        # print(str(pi_target)[:a + 2])   

    case 2: 
        print(f"Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")
                 
        def check_number_simple(n: int):
            i = 2
            while n % i != 0 or i == n - 1:
                i += 1
            if i == n:
                return n

        def fill_simple_list(n: int) -> list:
            simple_list = [1]
            for i in range(2, n+1):
                if n % i == 0:
                    if check_number_simple(i) != None:
                        simple_list.append(check_number_simple(i))
                else:
                    continue
            return simple_list


        # n = int(input('Введите натуральное число N: '))
        # simple_list = fill_simple_list(n)
        # print(simple_list)

        # n = int(input("Введите число N: "))
        # i = 2
        # list = []

        # while i <= n:
        #     if n % i == 0:
        #         list.append(i)
        #         n //= i
        #         i = 2
        # else:
        #     i += 1
        # print(f"Простые множители введенного числа указаны в списке: {list}")
        
    case 3: 
        print(f"Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов \nисходной последовательности.")

        string = '1 1 3 2 2 1 1 1 1'
        string = string.split()
        lst3 = []
        for i in range(0,len(string)):
            if  string[i] != string[i - 1]:
                lst3.append(i)
        print(lst3)

        # digits = [1, 2, 4, 5, 3, 2, 1, 1, 2, 4, 5, 7, 8]
        # dct = {}
        # for k in set(digits):
        #   dct.setdefault(k, digits.count(k))
        #   print(f'Неповторяющиеся элементы:', end=' ')
        # for k, v in dct.items():
        #   if int(v) == 1:
        # print(k, end=' ')

    case 4: 
        print("Задана натуральная степень k. Сформировать случайным образом список коэффициентов \n (значения от 0 до 100) многочлена и записать в файл многочлен степени k.")
        
        
        k = randint(1, 7) 
        filestr = str(randint(0, 100)) + ' = 0'
        for i in range(1, k + 1):
            num = randint(0, 100)
            if num > 0:
                if i == 1:
                    filestr = f'{num}*x + {filestr}'
                else:
                    filestr = f'{num}*x^{i} + {filestr}'
        filestr = f'k={k} => {filestr}\n'
        with open('zadacha4.txt', 'w') as datafile:
            datafile.writelines(filestr)



        # from random import randint

        # k = int(input('Insert equation power: '))
        # koefs = list()
        # for i in range(1, k + 2):
        #     koefs.append(randint(1, 100))

        # ans = list()
        # for i in range(len(koefs)):
        #     if k == 1:
        #         ans.append(f'{koefs[i]}*x')
        #     elif k == 0:
        #         ans.append(f'{koefs[i]}')
        #     else:
        #         ans.append(f'{koefs[i]}*x**{k}')
        #     flag = randint(0, 1)
        #     if flag == 1:
        #         ans.append('+')
        #     elif flag == 0:
        #         ans.append('-')
        #         k -= 1

        #     ans.pop(-1)
        #     ans.append('=0')
        #     fout = open('output.txt', 'w')
        #     fout.write(''.join(ans))
        #     fout.close()
       

    case 5: 
        print("Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.")

        # path = 'C:\Users\BOSS\Desktop\Base_Python\Hwork4\zadacha5_2.txt'
        # f = open(path, 'r')
        # data = f.read()
        # f.close()

        with open('zadacha5_1.txt', 'r') as datafile:
            left = datafile.readline()
        
        print(left)
        

        my_list = ["Pythonist.ru", "-", "хороший", "сайт", "по","Python"]
        print(" ".join(my_list))
        >>>Pythonist.ru - хороший сайт по Python
        # while data != '=0':
        #         left = data
        # print(data)

