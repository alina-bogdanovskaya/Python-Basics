# Задача 1
from sys import argv

hours, rate, bonus = map(float, argv[1:])


def salary_count(a, b, c):
    salary = (a * b) + c
    return salary


print(salary_count(hours, rate, bonus))

# Задача 2
from random import randint


def gen_list(r1, r2, n):
    my_random_list = []
    for i in range(n):
        num = randint(r1, r2)
        my_random_list.append(num)
    return my_random_list


random_list = gen_list(1, 11, 15)
print(random_list)

res_list = [random_list[i] for i in range(len(random_list)) if i == 0 or random_list[i] > random_list[i -1]]
print(res_list)

# Задача 3
res_list = [n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0]
print(res_list)

# Задача 4
def gen_list(r1, r2, n):
    my_random_list = []
    for i in range(n):
        num = randint(r1, r2)
        my_random_list.append(num)
    return my_random_list


random_list = gen_list(1, 4, 10)
print(random_list)


def unique(random_list):
    set_list = set()
    for k in random_list:
        if k not in set_list:
           set_list.add(k)
           yield(k)


unique_list = [k for k in unique(random_list)]
print(unique_list)

# Задача 5
from functools import reduce

one_more_list = [i for i in range(100, 1001) if i % 2 == 0]


def my_product(el, next_el):
    return el * next_el


print(reduce(my_product, one_more_list))

# Задача 6
from itertools import count, cycle

start = float(input("Please enter start point: "))
end = float(input("Please enter end point: "))
step = input("Please enter step or press Enter for 1: ")

if step == "":
    step = 1
else:
    step = float(step)

if int(step) == 0:
    print("Zero step not supported")
    exit(-1)

if start < end and step < 0:
    print("Cannot count to greater end with negative step")
    exit(-1)

if start > end and step > 0:
    print("Cannot count to lesser end with positive step")
    exit(-1)

for i in count (start, step):
    if start < end and i > end:
        break
    elif start > end and i < end:
        break
    else:
        print(i)

import string
import random

my_str_list = []

l = int(input("Please enter desired length of a string: "))
n = int(input("Please enter desired length of a list: "))
x = int(input("Please enter desired number of iterations: "))

for k in range(n):
    letters = string.ascii_letters
    my_str = ''.join(random.choice(letters) for i in range(l))
    my_str_list.append(my_str)

print(my_str_list)

y = 0
for el in cycle(my_str_list):
    if y > (x - 1):
        break
    else:
        print(el)
    y += 1

# Задача 7
n = int(input("Please enter integer: "))


def fact(n):
    factor = 1
    for el in range(1, n + 1):
        factor *= el
        yield factor


for el in fact(n):
    print(el)
