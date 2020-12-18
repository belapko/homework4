def iter1(a,b):
    my_list = []
    for i in range(a,b):
        my_list.append(i)
    return my_list
print(iter1(int(input("С какого числа начать: ")),int(input("По какое число: "))))




from itertools import cycle
my_list = list(input("Введите значения списка через пробел: ").split())
count = 0
number = input("Введите число повторений: ")
new_list = []
for i in cycle(my_list):
    if count == int(number):
        break
    new_list.append(my_list)
    count += 1
print(*new_list)
