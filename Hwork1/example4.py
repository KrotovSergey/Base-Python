# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

area = int(input('Задайте номер четверти: '))
if 0 < area < 5:
    if area == 1:
        print('x>0,y>0')
    elif area == 2:
        print(('x<0,y>0'))
    elif area == 3:
        print('x<0,y<0')
    elif area == 4:
        print('x>0,y<0')
    else:
        print( )
else:
    print('Неверный номер')5