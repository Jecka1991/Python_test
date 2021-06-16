X = float(input('x = '))
Y = float(input('y = '))
while True:
    sign = input("знак (+,-,*,/): ")
    if sign == '0':
        break
    elif sign in ('+', '-', '*', '/'):
        if sign == '+':
            print(X + Y)
        elif sign == '-':
            print(X - Y)
        elif sign == '*':
            print(X * Y)
        elif sign == '/':
            if Y != 0:
                print(X / Y)
            else:
                print('Нельзя делить на ноль!!!')


number = int(input('Введите число '))
sum = 0
mult = 1
while number > 0:
    sum += number % 10
    mult *= number % 10
    number = number // 10

print('Сумма цифр: ', sum)
print('Произведение цифр: ', mult)


import random
n = int(input())
sum = 0
matrix = [[random.randrange(0,10) for i in range(n)] for j in range(n)]
print(matrix)

new = int(input())
sum = 0
matrix = [[random.randrange(0, 10) for i in range(new)] for j in range(new)]
print(matrix)
for x in matrix:
    for y in x:
        if y % 3 == 0:
            sum += sum + y

print(sum)