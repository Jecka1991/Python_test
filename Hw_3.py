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
