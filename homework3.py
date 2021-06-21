# Задача 1
num = float(input("Please enter numerator: "))
denom = float(input("Please enter denominator: "))


def my_div(num, denom):
    if denom == 0:
        return
    return num / denom


print(my_div(num, denom))

# Задача 2
def user_data (name, last_name, phone, city, yob, email):
    print(name, last_name, yob, city, email, phone)


name = input("Введите имя: ")
phone = input("Введите телефон: ")
yob = input("Введите год рождения: ")
email = input("Введите email: ")
city = input("Введите город проживания: ")
last_name = input("Введите фамилию: ")

user_data(name = name, last_name = last_name, phone = phone, city = city, yob = yob, email = email)

# Задача 3
a = float(input("Введите значение: "))
b = float(input("Введите значение: "))
c = float(input("Введите значение: "))


def my_func(a, b, c):
    min_val = min(a, b, c)
    if a == min_val:
        my_sum = b + c
    elif b == min_val:
        my_sum = a + c
    else:
        my_sum = a + b
    return(my_sum)


my_func(a, b, c)
print(my_func(a, b, c))

# Задача 4
x = float(input("Please enter real positive number: "))
y = int(input("Please enter negative integer: "))

def my_func(x, y):
    return(x ** y)


def my_func(x, y):
    abs_y = abs(y)
    while abs_y > 1:
        abs_y -= 1
        x = x * x
    return 1 / x


def my_func(x, y):
    for i in range(1, abs(y)):
        x = x * x
    return 1 / x


print(my_func(x, y))

# Задача 5
num_sum = 0

while True:
    nums = input("Please enter several numbers, enter # to complete: ")
    num_list = nums.strip().split(' ')

    for el in num_list:
        if el == "#":
            break
        else:
            num_sum += float(el)

    print(num_sum)

    if el == "#":
        break

# Задача 6
s1 = input("Please type any word or few words: ")


def int_func(s1):
    s_new = s1.title()
    return s_new


def int_func(s1):
    new_list = s1.split(' ')
    new_str = ""
    for el in new_list:
        a = el[:1]
        a = ord(a) - 32
        b = el[1:]
        new_str = f'{new_str} {(chr(a) + b)}'
    return new_str


print(int_func(s1))



