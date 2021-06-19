# Задача 1
n = 23
list1 = ['hey you', n, (4, 8, 13), '37', True, 18.5]
print(type(list1))
for item in list1:
    print(type(item))

# Задача 2
el = ''
dum_list = []
while True:
    el = input('Type something, to complete type "end" ')
    if el == "end":
        break
    dum_list.append(el)

print(dum_list)

for index in range(0, len(dum_list) -1, 2):
        dum_list[index + 1], dum_list[index] = dum_list[index], dum_list[index + 1]
print(dum_list)

# Задача 3
month = int(input('Enter month number 1 - 12 '))

di = {1:'winter', 2:'winter', 3:'spring', 4:'spring', 5:'spring', 6:'summer', 7:'summer', 8:'summer', 9:'fall', 10:'fall', 11:'fall', 12:'winter'}
a = di.get(month)

if a is not None:
    print(a)
else:
    print("Incorrect value")

li = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'fall', 'fall', 'fall', 'winter']
if 0 < month <= 12:
    print(li[month -1])
else:
    print("Incorrect value")

# Задача 4
s1 = input('Type anything ')
l1 = s1.split(' ')
# print(l1)

for index in range(len(l1)):
    item = l1[index]
    if len(item) > 10:
        print(f'{index + 1} {item[:10]}')
    else:
        print(f'{index + 1} {item}')

# Задача 5
list1 = [7, 6, 2]

while True:
    a = int(input("Enter number: "))

    if a < 1:
        print("Invalid value")
        exit(-1)

    if a <= list1[len(list1) - 1]:
        list1.append(a)
        print(list1)
        continue

    for index in range(len(list1)):
        if a > list1[index]:
            list1.insert(index, a)
            print(list1)
            break

# Задача 6
lst = []
i = 0
good_key = 'наименование'
price_key = 'цена'
quant_key = 'количество'
unit_key = 'единицы'

while True:
    good = input("Введите наименование товара или нажмите Enter чтобы закончить: ")
    if good == "":
        break

    price = input("Введите цену товара: ")
    quantity = input("Введите количество товара: ")
    unit = input("Введите единицы измерения: ")

    i += 1

    new_item = (i, {good_key: good, price_key: price, quant_key: quantity, unit_key: unit})
    lst.append(new_item)
#     print(lst)

my_dict = {}

for tpl in lst:
    dct = tpl[1]

    for key in dct.keys():
        val = dct[key]
        val_list = my_dict.setdefault(key, [])
        val_list.append(val)

print(my_dict)
