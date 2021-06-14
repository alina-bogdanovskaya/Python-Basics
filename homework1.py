# Задача 1
a = 8
b = 18
c = "London is the capital of Great Britain"
print(type(a))
print(type(c))
b = str(b)
print(type(b))

name = input('Enter your name here: ')
age = input('Enter your age here: ')
age = int(age)
print("Hello " + name)
print(f'name - {name}, age - {age}')

if age >= 21:
    print('Welcome to the iLand ' + name)
else:
    print("Go fishing")

# Задача 2
prompt_msg = 'Enter time in seconds: '
sec_input = input(prompt_msg)
while not sec_input.isdigit():
    print('Please enter valid positive numeric value')
    sec_input = input(prompt_msg)

sec_input = int(sec_input)
minutes = (sec_input % 3600) // 60
seconds = sec_input % 60
hours = sec_input // 3600

seconds = sec_input % 60
minutes = sec_input // 60
hours = minutes // 60
minutes = ((sec_input // 60) - minutes // 60 * 60)

print(f'{hours:02}:{minutes:02}:{seconds:02}')

# Задача 3
n = input('Enter any number: ')

while not n.isdigit():
    print("Please enter valid positive number")
    n = input('Enter any number: ')

a = int(n + n)
b = int(n + n + n)
n = int(n)
print(f'{n} + {a} + {b} = {n + a + b}')

# Задача 4
num = int(input('Enter whole positive number: '))
n = 0

while num > 0:
    a = num % 10
    if n < a:
        n = a
    num = int(num // 10)

print(f'The largest digit is {n}')

# Задача 5
rev =  float(input('Enter company\'s revenue: '))
exps = float(input('Enter company\'s expenses: '))

if rev > exps:
    print('Your performance: profit')
    profit = rev - exps
    margin = profit / rev * 100
    print(f'Profit margin = {margin:.2f}%')
    empl = int(input('Enter number of employees: '))
    n = profit / empl
    print('Profit per employee = ' + str(n))

else:
    print('Your performance: loss')

# Задача 6
a = float(input('Enter first day value: '))
b = float(input('Enter target value: '))
i = 1
while a < b:
    a += a * 10 / 100
    i += 1
print(i)