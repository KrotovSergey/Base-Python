s = input('Введите число: ')
sm = 0
for i in s:
    if i != '.' and i != ',':
        sm += int(i)
print('Сумма цифр:', sm)