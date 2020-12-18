from functools import reduce
# for i in range(100,1001):
#     if i % 2 == 0:
#         my_list.append(i)
# print(my_list)
my_list = [i for i in range(100,1001) if i % 2 == 0]
product = reduce(lambda a,b: a*b, my_list)
print(product)