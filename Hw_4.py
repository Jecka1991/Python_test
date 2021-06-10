test_list = [1, 3, 4, 6, 10]
new_list = [i * -2 for i in test_list]

print(new_list)


a_list = [1, 2, 5, 6, 7, 12, 124]
b_list = [i for i in a_list if i % 2 == 0]

print(b_list)


my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(my_dict.keys()) :
    my_dict[key + str(len(key))] = my_dict.pop(key)

print(my_dict)


a_list = [1, 2, 5, 6, 7, 12, 124]
b_list = a_list[-1]
for i, c_list in enumerate(a_list):
    a_list[i], b_list = b_list, c_list

print(a_list)


a = 1
b = 1
Fibo = [a , b]
for i in range(13):
    a, b = b, a+b
    Fibo.append(b)

print(Fibo)

# 4.04
n = int(input())
sum = 0
val = 1
while val <= n:
    sum += val ** 3
    val += 1

print(sum)


# 4.06
a = int(input())
b = int(input())
c = a + 1
sum = 0

for i in range(c, b):
  sum += i ** 3
  print(sum)


# 4.07
a = int(input())
b = int(input())
n = (range(a, b +1))

if a < b:
  print(sorted(range(a, b +1)))
  print(len(n))


# 4.01
r_list = list(range(21))
sum = 0
for values in r_list:
  if values > 10:
    sum += values

print(sum)

# 4.02
text = input()
total = 0
while text != 'stop':
    num = int(text)
    total += num
    text = input()

print(total)

a = 1
b = 1
Fibo = [a , b]
for i in range(13):
    a, b = b, a+b
    Fibo.append(b)
print(Fibo)

# 4.04
n = int(input())
sum = 0
val = 1
while val <= n:
    sum += val ** 3
    val += 1

print(sum)