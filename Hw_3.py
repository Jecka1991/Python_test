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



