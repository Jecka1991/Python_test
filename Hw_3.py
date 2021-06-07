number = 5000
if number % 1000 == 0:
    print("millennium")

number_of_guests = 33
if number_of_guests > 50:
    print('restaurant')
elif number_of_guests >= 20:
    print('cafe')
else:
    print('home')

string = "Hello, my dear friend"
if len(string) > 10:
    print(string + '!!!')
else:
    print(string[1])

string = "Hello, my dear friend"
mid = int(len(string) / 2)
print(string[mid])
if string[mid] == string[0]:
    print(string[1:-1])

name = input('input your name ')
print('Hello, ' + name + '!')

first_number = int(input('input first number '))
second_number = int(input('input second number '))
summ = first_number + second_number
print(str(first_number) + '+' + str(second_number) + '=' + str(summ))

string_new = input('input two word ')
string_new_list = string_new.split(' ')
print('!' + string_new_list[1] + ' ' + string_new_list[0] + '!')

quote = 'No money, no honey'
length = len(quote)
if length % 3 == 0:
    print(quote + '!')

quote_2 = 'This is SPARTA!'
if 'code' in quote_2:
    print('Yes')
else:
    print('No')

age = int(input('input your age, please '))
if age < 0:
    print('Wrong input')
elif age < 18:
    print('CocaCola')
else:
    print('Beer')

value = input('input string ')
length = int(len(value))
if length > 5:
    print(length)
elif length < 5:
    print('Need more!')
else:
    print('It is five')

number_one = (input('input your happy number '))
if number_one.isdigit():
    print(int(number_one) ** 3)

import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")

how_ruble = input('Введите количество рублей ')
d = int(how_ruble[-2:])
a = int(how_ruble[-1])
c = int(how_ruble)
how_penny = input('Введите количество копеек ')

if d > 10 and d < 20:
    print(str(c) + ' рублей')
elif a == 1:
    print(str(c) + ' рубль')
elif a > 1 and a < 5:
    print(str(c) + ' рубля')
elif a == 0:
 print(str(c) + ' рублей')
else:
  print(str(c) + ' рублей')

f = int(how_penny[-2:])
e = int(how_penny[-1])
b = int(how_penny)

if d > 10 and d < 20:
  print(str(b) + ' копеек')
elif e > 1 and e < 5:
  print(str(b) + ' копейки')
elif e == 0:
  print(str(b) + ' копеек')
elif e == 1:
  print(str(b) + ' копейка')
else:
 (str(b) + ' копеек')





