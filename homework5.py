# Задача 1
try:
    with open('new_file.txt', 'w', encoding='utf8') as f:
        while True:
            content = input("Please enter your data: ")
            if content == "":
                break
            else:
                f.write(content + '\n')
except IOError:
    print('Input output error')

with open('new_file.txt', 'r', encoding='utf8') as file:
    for line in file:
        print(line, end='')

# Задача 2
try:
    with open("new_file.txt", "r", encoding='utf8') as file:
        num_lines = 0
        num_words = 0
        num_chr = 0
        for line in file:
            line = line.strip("\n")
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chr += len(line)
except IOError as err:
    print(f'IOError: {err}')

print("lines:", num_lines, "words:", num_words, "characters:", num_chr)

# Задача 3
try:
    with open('salary_per_employee.txt', 'r', encoding='utf8') as sal:
        num_lines = 0
        sal_sum = 0
        for line in sal:
            line = line.strip("\n")
            num_lines += 1
            emp_sal = line.split()
            x = int(emp_sal[1])
            if x < 20000:
                print(emp_sal[0])
            sal_sum += x

except IOError as err:
    print(f'IOError: {err}')

print(f"Средняя величина дохода: {sal_sum / num_lines}")

# Задача 4
my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'}

try:
    with open('eng_numbers.txt', 'r', encoding='utf8') as num_eng:
        with open('rus_numbers.txt', 'w', encoding='utf8') as num_rus:
            for line in num_eng:
                list_line = line.split()
                a = list_line[0]
                b = my_dict.get(a)
                line_new = line.replace(a, b)
                num_rus.write(line_new)
except IOError as err:
    print(f'IOError: {err}')

with open('rus_numbers.txt', 'r', encoding='utf8') as num_rus:
    print(num_rus.read())

# Задача 5
try:
    with open('new_num_file.txt', 'w+') as num_file:
        x = '2 12 85 0 6'
        num_file.write(x)
        num_file.seek(0)
        num_list = num_file.read().split()
        num_sum = 0
        for num in num_list:
            num_sum += int(num)
        print(num_sum)
except IOError as err:
    print(f'IOError: {err}')

# Задача 6
from re import sub

try:
    my_class_dict = {}
    with open("classes.txt", "r") as classes:
        for line in classes:
            my_list = line.split()
            key = my_list[0]
            key = key[:-1]
            value_list = my_list[1:]
            hours = 0
            for i in value_list:
                if i != '-':
                    i = int(sub('\(.*?\)', '', i))
                    hours += i
            my_class_dict[key] = hours
except IOError as err:
    print(f'IOError: {err}')

print(my_class_dict)

# Задача 7
import json

comp_profit = {}
avg_profit = {}
dict_list = []

try:
    with open('companies.txt', 'r') as companies:
        sum_profit = 0
        num_lines = 0
        for line in companies:
            line = line.strip('\n')
            num_lines += 1
            my_list = line.split()
            key = my_list[0]
            profit = int(my_list[2]) - int(my_list[3])
            if profit > 0:
                sum_profit += profit
            comp_profit[key] = profit
            x = sum_profit / num_lines
            avg_profit["average profit"] = x
        dict_list.append(comp_profit)
        dict_list.append(avg_profit)
        print(dict_list)
except IOError as err:
    print(f'IOError: {err}')

with open('companies.json', 'w') as w_f:
    json.dump(dict_list, w_f)